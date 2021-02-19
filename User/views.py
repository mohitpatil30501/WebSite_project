import base64
import datetime
import json

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import *
from WebSite.settings import SECRET_KEY


def student_create(request):
    if request.method == "POST":
        prn = request.POST.get('prn')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mother_name = request.POST.get('mother_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Student.objects.filter(college_data__prn=prn, college_data__mother_name=mother_name).count() != 0:
            return render(request, "error/index.html",
                          {'error': 'Something Went Wrong', 'message': "PRN already exist, Try to LogIn"})

        if User.objects.filter(username=username).count() != 0:
            return render(request, "error/index.html",
                          {'error': 'Something Went Wrong', 'message': "User Already Exist"})

        try:
            student_data = CollegeStudentData.objects.filter(prn=prn, mother_name=mother_name).get()
        except:
            return render(request, "error/index.html",
                          {'error': 'Something Went Wrong',
                           'message': "College Data is Not Satisfies like: Prn, Mother Name"})

        try:
            user = User.objects.create_user(username, email=email, first_name=first_name,
                                            last_name=last_name, password=password)
        except:
            return render(request, "error/index.html",
                          {'error': 'Something Went Wrong',
                           'message': "Some data is Not Satisfies like: Username, Password, Email"})

        email_status = email_confirmation_send_to_student(user, request)
        if email_status:
            Student.objects.create(student=user, college_data=student_data)
            user.is_active = False
            user.save()

            return render(request, "User/email.html", {'status': True,
                                                       'email_status': True,
                                                       'message': "Account created Successfully...."
                                                       })
        else:
            user.delete()
            return render(request, "error/index.html",
                          {'error': 'Email Server Down',
                           'message': "Problem to send email...!"})

    return render(request, "error/index.html",
                  {'error': 'Wrong Method',
                   'message': "Only POST method Allowed"})


def auth_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).count() == 0:
            messages.error(request, 'User Not Exist.')
            return render(request, "Website/index.html")

        try:
            user = User.objects.filter(username=username).get()
            if not user.is_active:
                user_data = Student.objects.filter(student=user).get()
                if not user_data.email_verification:
                    return render(request, "error/index.html",
                                  {'error': 'Verify Email First',
                                   'message': "Email is Not Verified..!"})
                return render(request, "error/index.html",
                              {'error': 'Inactive User',
                               'message': "User is InActive..!"})
        except:
            return render(request, "error/index.html",
                          {'error': 'Data Problem',
                           'message': "Failed to Extract Data..!"})

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Incorrect Password')
            return render(request, "Website/index.html")

        login(request, user)
        return redirect('/dashboard')

    return render(request, "error/index.html",
                  {'error': 'Wrong Method',
                   'message': "Only POST method Allowed"})


def auth_logout(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            logout(request)
            return redirect('/')

        return redirect('/')

    return render(request, "error/index.html",
                  {'error': 'Wrong Method',
                   'message': "Only POST method Allowed"})


# Email Student
def key_maker(username):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'\xcfz\xfc\xdcF\xc1d\xc1\xb4\xfa5%\xe7\xa5\x14\x16',
        iterations=100000,
        backend=default_backend()
    )
    return Fernet(base64.urlsafe_b64encode(kdf.derive(str(SECRET_KEY + username[::-1]).encode())))


def email_confirmation_send_to_student(user, request):
    # Key Making
    key = key_maker(user.username)

    # Collect Data
    # url : username={username}&data={encrypted data} //valid for 3 days

    data = {
        "username": user.username,
        "valid_time": str(datetime.datetime.today() + datetime.timedelta(days=3))
    }
    data = key.encrypt(json.dumps(data).encode()).decode()
    url = request.build_absolute_uri('?') + "/email_verification/" + user.username + "/" + data

    message = '''
    <!DOCTYPE html>
    <html>
    <head>
    </head>
    <body>
        <h1>SSBT</h1>
        <h3>Email Verification</h3>
        <form method="GET" action="''' + str(url) + ''''">
            <button type="submit">Click to Verify</button>
        </form>
        <hr>
        <p>Valid for 30 min only</p>
        <h2>If this mail is not relatable, Please Do not Click to Verify...!</h2>
    </body>
    </html>
    '''

    try:
        send_mail("Email Verification", "", "SSBT", [user.email, ], fail_silently=False, html_message=message)
        return True
    except:
        return False


def email_verifcation_of_student(request, username, data):
    # Key Making
    key = key_maker(username)
    try:
        data = key.decrypt(data.encode()).decode()
        data = json.loads(data)

        valid_time = datetime.datetime.strptime(data["valid_time"], '%Y-%m-%d %H:%M:%S.%f')

        if datetime.timedelta(0) <= valid_time - datetime.datetime.today() <= datetime.timedelta(3) and username == \
                data['username']:
            # change state to Active
            try:
                user = User.objects.filter(username=username).get()
                user.is_active = True
                user.save()
                student_data = Student.objects.filter(student=user).get()
                student_data.email_verification = True
                student_data.save()
            except:
                return render(request, "error/index.html",
                              {'error': 'Data Problem',
                               'message': "Unable to Extract user data...!"})
            return redirect('/')
            # return JsonResponse({
            #     'username': username,
            #     'data': data,
            #     'valid_status': True
            # })
        return render(request, "error/index.html",
                      {'error': 'Expired Link',
                       'message': "Link is Not Valid...!"})
    except:
        return render(request, "error/index.html",
                      {'error': 'Something went wrong',
                       'message': "Something went wrong...!"})
