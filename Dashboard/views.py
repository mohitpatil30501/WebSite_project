import json

from django.shortcuts import render, redirect

from .models import *


def dashboard(request):
    if request.user.is_authenticated:
        try:
            details_object = Details.objects.filter(teacher__teacher=request.user).get()

            designation_object = Designation.objects.filter(teacher__teacher=request.user).get()

            subject_of_interest_list = []
            for subject in SubjectOfInterest.objects.filter(teacher__teacher=request.user).order_by('index'):
                subject_of_interest_list.append({
                    'teacher': str(subject.teacher.id),
                    'id': str(subject.id),
                    'subject_of_interest': subject.subject_of_interest,
                })

            academics = []
            for academic in Academics.objects.filter(teacher__teacher=request.user).order_by('index'):
                academics.append({
                    'teacher': str(academic.teacher.id),
                    'id': str(academic.id),
                    'degree': academic.degree,
                    'specialisation': academic.specialisation,
                    'university': academic.university,
                    'year': academic.year,
                    'remarks': academic.remarks,
                })

            memberships = []
            for membership in ProfessionalMembership.objects.filter(teacher__teacher=request.user).order_by('index'):
                memberships.append({
                    'teacher': str(membership.teacher.id),
                    'id': str(membership.id),
                    'society': membership.society,
                    'ist_no': membership.ist_no,
                    'date_of_membership': membership.date_of_membership,
                })

            institutes = []
            for institute in TeachingExperience.objects.filter(teacher__teacher=request.user).order_by('index'):
                institutes.append({
                    'teacher': str(institute.teacher.id),
                    'id': str(institute.id),
                    'name': institute.name,
                    'designation': institute.designation,
                    'date_of_join': institute.date_of_join,
                    'date_of_leave': institute.date_of_leave,
                })

            administratives = []
            for administrative in AdministrativeExperience.objects.filter(teacher__teacher=request.user).order_by(
                    'index'):
                administratives.append({
                    'teacher': str(administrative.teacher.id),
                    'id': str(administrative.id),
                    'name': administrative.name,
                    'designation': administrative.designation,
                    'date_of_join': administrative.date_of_join,
                    'date_of_leave': administrative.date_of_leave,
                })

            industrys = []
            for industry in IndustrialExperience.objects.filter(teacher__teacher=request.user).order_by(
                    'index'):
                industrys.append({
                    'teacher': str(industry.teacher.id),
                    'id': str(industry.id),
                    'name': industry.name,
                    'designation': industry.designation,
                    'date_of_join': industry.date_of_join,
                    'date_of_leave': industry.date_of_leave,
                })

            facultys = []
            for faculty in FacultyDevelopment.objects.filter(teacher__teacher=request.user).order_by(
                    'index'):
                facultys.append({
                    'teacher': str(faculty.teacher.id),
                    'id': str(faculty.id),
                    'name': faculty.name,
                    'designation': faculty.designation,
                    'date_of_approval': faculty.date_of_approval,
                })
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
            },
            'designation': {
                'designation': {
                    'teacher': str(designation_object.teacher.id),
                    'id': str(designation_object.id),
                    'designation': designation_object.designation if designation_object.designation is not None else '',
                    'department': designation_object.department if designation_object.department is not None else '',
                    'institute': designation_object.institute if designation_object.institute is not None else '',
                },
                'subject_of_interest': subject_of_interest_list,
                'academics': academics,
                'memberships': memberships,
                'institutes': institutes,
                'administratives': administratives,
                'industrys': industrys,
                'facultys': facultys,
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
            for subject in SubjectOfInterest.objects.filter(teacher__teacher=request.user).order_by('index'):
                subject_of_interest_list.append({
                    'teacher': str(subject.teacher.id),
                    'id': str(subject.id),
                    'subject_of_interest': subject.subject_of_interest,
                })

            academics = []
            for academic in Academics.objects.filter(teacher__teacher=request.user).order_by('index'):
                academics.append({
                    'teacher': str(academic.teacher.id),
                    'id': str(academic.id),
                    'degree': academic.degree,
                    'specialisation': academic.specialisation,
                    'university': academic.university,
                    'year': academic.year,
                    'remarks': academic.remarks,
                })

            memberships = []
            for membership in ProfessionalMembership.objects.filter(teacher__teacher=request.user).order_by('index'):
                memberships.append({
                    'teacher': str(membership.teacher.id),
                    'id': str(membership.id),
                    'society': membership.society,
                    'ist_no': membership.ist_no,
                    'date_of_membership': membership.date_of_membership,
                })

            institutes = []
            for institute in TeachingExperience.objects.filter(teacher__teacher=request.user).order_by('index'):
                institutes.append({
                    'teacher': str(institute.teacher.id),
                    'id': str(institute.id),
                    'name': institute.name,
                    'designation': institute.designation,
                    'date_of_join': institute.date_of_join,
                    'date_of_leave': institute.date_of_leave,
                })

            administratives = []
            for administrative in AdministrativeExperience.objects.filter(teacher__teacher=request.user).order_by('index'):
                administratives.append({
                    'teacher': str(administrative.teacher.id),
                    'id': str(administrative.id),
                    'name': administrative.name,
                    'designation': administrative.designation,
                    'date_of_join': administrative.date_of_join,
                    'date_of_leave': administrative.date_of_leave,
                })

            industrys = []
            for industry in IndustrialExperience.objects.filter(teacher__teacher=request.user).order_by(
                    'index'):
                industrys.append({
                    'teacher': str(industry.teacher.id),
                    'id': str(industry.id),
                    'name': industry.name,
                    'designation': industry.designation,
                    'date_of_join': industry.date_of_join,
                    'date_of_leave': industry.date_of_leave,
                })

            facultys = []
            for faculty in FacultyDevelopment.objects.filter(teacher__teacher=request.user).order_by(
                    'index'):
                facultys.append({
                    'teacher': str(faculty.teacher.id),
                    'id': str(faculty.id),
                    'name': faculty.name,
                    'designation': faculty.designation,
                    'date_of_approval': faculty.date_of_approval,
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
            'academics': academics,
            'memberships': memberships,
            'institutes': institutes,
            'administratives': administratives,
            'industrys': industrys,
            'facultys': facultys,
        }
        return render(request, "Dashboard/designation.html", {'data': data})
    return redirect('/')


def edit_activity(request):
    if request.user.is_authenticated:
        return render(request, "Dashboard/activity.html")
    return redirect('/')
