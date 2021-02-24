import json

from django.shortcuts import render, redirect

from .models import *


def dashboard(request):
    if request.user.is_authenticated:
        try:
            details_object = Details.objects.filter(teacher__teacher=request.user).get()
        except:
            return redirect('/')

        data = {
            'details': {
                'teacher': str(details_object.teacher.id),
                'id': str(details_object.id),
                'name': details_object.name,
                'website': details_object.website,
                'email': details_object.email,
                'phone': details_object.phone,
                'mobile': details_object.mobile,
                'address': details_object.address,
                'date_of_birth': details_object.date_of_birth,
            }
        }
        return render(request, "Dashboard/dashboard.html", data)
    return redirect('/')


def edit_details(request):
    if request.user.is_authenticated:
        try:
            details_object = Details.objects.filter(teacher__teacher=request.user).get()
        except:
            return redirect('/dashboard')

        data = {
            'teacher': str(details_object.teacher.id),
            'id': str(details_object.id),
            'name': details_object.name,
            'website': details_object.website if details_object.website is not None else '',
            'email': details_object.email,
            'phone': details_object.phone if details_object.phone is not None else '',
            'mobile': details_object.mobile if details_object.mobile is not None else '',
            'address': details_object.address if details_object.address is not None else '',
            'date_of_birth': details_object.date_of_birth if details_object is not None else '',
        }
        return render(request, "Dashboard/details.html", {'data': data})
    return redirect('/')


def edit_designation(request):
    if request.user.is_authenticated:
        try:
            designation_object = Designation.objects.filter(teacher__teacher=request.user).get()

            subject_of_interest_list = []
            for subject in SubjectOfInterest.objects.filter(teacher__teacher=request.user):
                subject_of_interest_list.append({
                    'teacher': str(subject.teacher.id),
                    'id': str(subject.id),
                    'subject_of_interest': subject.subject_of_interest,
                })

        except:
            return redirect('/dashboard')

        data = {
            'designation': {
                'teacher': str(designation_object.teacher.id),
                'id': str(designation_object.id),
                'designation': designation_object.designation if designation_object.designation is not None else '',
                'department': designation_object.department if designation_object.department is not None else '',
                'institute': designation_object.institute if designation_object.institute is not None else '',
            },
            'subject_of_interest': subject_of_interest_list,
        }
        return render(request, "Dashboard/designation.html", {'data': data})
    return redirect('/')


def edit_activity(request):
    if request.user.is_authenticated:
        return render(request, "Dashboard/activity.html")
    return redirect('/')
