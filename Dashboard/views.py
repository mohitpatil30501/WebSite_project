import json

from django.http import JsonResponse
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

            publications_book = []
            for book in PublicationsBook.objects.filter(teacher__teacher=request.user).order_by('index'):
                publications_book.append({
                    'teacher': str(book.teacher.id),
                    'id': str(book.id),
                    'name': book.name,
                    'publication': book.publication,
                    'year': book.year,
                })

            publications_journal = []
            for journal in PublicationsJournal.objects.filter(teacher__teacher=request.user).order_by('index'):
                publications_journal.append({
                    'teacher': str(journal.teacher.id),
                    'id': str(journal.id),
                    'name': journal.name,
                    'title': journal.title,
                    'publication': journal.publication,
                    'page': journal.page,
                    'year': journal.year,
                    'url': journal.url,
                    'level': journal.level,
                })

            publications_paper = []
            for paper in PublicationsPaper.objects.filter(teacher__teacher=request.user).order_by('index'):
                publications_paper.append({
                    'teacher': str(paper.teacher.id),
                    'id': str(paper.id),
                    'name': paper.name,
                    'title': paper.title,
                    'publication': paper.publication,
                    'year': paper.year,
                    'url': paper.url,
                    'level': paper.level,
                })

            sttps = []
            for sttp in ShortTermsTrainingProgram.objects.filter(teacher__teacher=request.user).order_by('index'):
                sttps.append({
                    'teacher': str(sttp.teacher.id),
                    'id': str(sttp.id),
                    'name': sttp.name,
                    'organization': sttp.organization,
                    'year': sttp.year,
                    'date_form': sttp.date_form,
                    'date_to': sttp.date_to,
                    'day': sttp.day,
                })

            workshops = []
            for workshop in Workshops.objects.filter(teacher__teacher=request.user).order_by('index'):
                workshops.append({
                    'teacher': str(workshop.teacher.id),
                    'id': str(workshop.id),
                    'name': workshop.name,
                    'organization': workshop.organization,
                    'year': workshop.year,
                    'date_form': workshop.date_form,
                    'date_to': workshop.date_to,
                    'day': workshop.day,
                })

            oiis = []
            for oii in OtherInstituteInteractions.objects.filter(teacher__teacher=request.user).order_by('index'):
                oiis.append({
                    'teacher': str(oii.teacher.id),
                    'id': str(oii.id),
                    'organization': oii.organization,
                    'year': oii.year,
                    'invitee': oii.invitee,
                })

            consultancys = []
            for consultancy in Consultancy.objects.filter(teacher__teacher=request.user).order_by('index'):
                consultancys.append({
                    'teacher': str(consultancy.teacher.id),
                    'id': str(consultancy.id),
                    'organization': consultancy.organization,
                    'year': consultancy.year,
                    'work_done': consultancy.work_done,
                    'cost': consultancy.cost,
                })

            awards = []
            for award in AwardReceived.objects.filter(teacher__teacher=request.user).order_by('index'):
                awards.append({
                    'teacher': str(award.teacher.id),
                    'id': str(award.id),
                    'organization': award.organization,
                    'year': award.year,
                    'title': award.title,
                })

            projects = []
            for project in ProjectGuided.objects.filter(teacher__teacher=request.user).order_by('index'):
                projects.append({
                    'teacher': str(project.teacher.id),
                    'id': str(project.id),
                    'name': project.name,
                    'year': project.year,
                    'level': project.level,
                })

            ecas = []
            for eca in ExtraCurricularActivities.objects.filter(teacher__teacher=request.user).order_by('index'):
                ecas.append({
                    'teacher': str(eca.teacher.id),
                    'id': str(eca.id),
                    'name': eca.name,
                    'year': eca.year,
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
                'profile_pic': {
                    'status': 1 if bool(details_object.profile_file) else 0,
                    'url': details_object.profile_file.url if bool(details_object.profile_file) else '',
                }
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
            },
            'activity': {
                'publications_book': publications_book,
                'publications_journal': publications_journal,
                'publications_paper': publications_paper,
                'sttps': sttps,
                'workshops': workshops,
                'oiis': oiis,
                'consultancys': consultancys,
                'awards': awards,
                'projects': projects,
                'ecas': ecas,
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
            'date_of_birth': details_object.date_of_birth if details_object.date_of_birth is not None else '',
            'profile_pic': {
                'status': 1 if bool(details_object.profile_file) else 0,
                'url': details_object.profile_file.url if bool(details_object.profile_file) else '',
            }
        }
        return render(request, "Dashboard/details.html", {'data': data})
    return redirect('/')


def edit_designation(request):
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
            return redirect('/dashboard')

        data = {
            'details': {
                'profile_pic': {
                    'status': 1 if bool(details_object.profile_file) else 0,
                    'url': details_object.profile_file.url if bool(details_object.profile_file) else '',
                }
            },
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
        try:
            details_object = Details.objects.filter(teacher__teacher=request.user).get()

            designation_object = Designation.objects.filter(teacher__teacher=request.user).get()

            publications_book = []
            for book in PublicationsBook.objects.filter(teacher__teacher=request.user).order_by('index'):
                publications_book.append({
                    'teacher': str(book.teacher.id),
                    'id': str(book.id),
                    'name': book.name,
                    'publication': book.publication,
                    'year': book.year,
                })

            publications_journal = []
            for journal in PublicationsJournal.objects.filter(teacher__teacher=request.user).order_by('index'):
                publications_journal.append({
                    'teacher': str(journal.teacher.id),
                    'id': str(journal.id),
                    'name': journal.name,
                    'title': journal.title,
                    'publication': journal.publication,
                    'page': journal.page,
                    'year': journal.year,
                    'url': journal.url,
                    'level': journal.level,
                })

            publications_paper = []
            for paper in PublicationsPaper.objects.filter(teacher__teacher=request.user).order_by('index'):
                publications_paper.append({
                    'teacher': str(paper.teacher.id),
                    'id': str(paper.id),
                    'name': paper.name,
                    'title': paper.title,
                    'publication': paper.publication,
                    'year': paper.year,
                    'url': paper.url,
                    'level': paper.level,
                })

            sttps = []
            for sttp in ShortTermsTrainingProgram.objects.filter(teacher__teacher=request.user).order_by('index'):
                sttps.append({
                    'teacher': str(sttp.teacher.id),
                    'id': str(sttp.id),
                    'name': sttp.name,
                    'organization': sttp.organization,
                    'year': sttp.year,
                    'date_form': sttp.date_form,
                    'date_to': sttp.date_to,
                    'day': sttp.day,
                })

            workshops = []
            for workshop in Workshops.objects.filter(teacher__teacher=request.user).order_by('index'):
                workshops.append({
                    'teacher': str(workshop.teacher.id),
                    'id': str(workshop.id),
                    'name': workshop.name,
                    'organization': workshop.organization,
                    'year': workshop.year,
                    'date_form': workshop.date_form,
                    'date_to': workshop.date_to,
                    'day': workshop.day,
                })

            oiis = []
            for oii in OtherInstituteInteractions.objects.filter(teacher__teacher=request.user).order_by('index'):
                oiis.append({
                    'teacher': str(oii.teacher.id),
                    'id': str(oii.id),
                    'organization': oii.organization,
                    'year': oii.year,
                    'invitee': oii.invitee,
                })

            consultancys = []
            for consultancy in Consultancy.objects.filter(teacher__teacher=request.user).order_by('index'):
                consultancys.append({
                    'teacher': str(consultancy.teacher.id),
                    'id': str(consultancy.id),
                    'organization': consultancy.organization,
                    'year': consultancy.year,
                    'work_done': consultancy.work_done,
                    'cost': consultancy.cost,
                })

            awards = []
            for award in AwardReceived.objects.filter(teacher__teacher=request.user).order_by('index'):
                awards.append({
                    'teacher': str(award.teacher.id),
                    'id': str(award.id),
                    'organization': award.organization,
                    'year': award.year,
                    'title': award.title,
                })

            projects = []
            for project in ProjectGuided.objects.filter(teacher__teacher=request.user).order_by('index'):
                projects.append({
                    'teacher': str(project.teacher.id),
                    'id': str(project.id),
                    'name': project.name,
                    'year': project.year,
                    'level': project.level,
                })

            ecas = []
            for eca in ExtraCurricularActivities.objects.filter(teacher__teacher=request.user).order_by('index'):
                ecas.append({
                    'teacher': str(eca.teacher.id),
                    'id': str(eca.id),
                    'name': eca.name,
                    'year': eca.year,
                })
        except:
            return redirect('/dashboard')

        data = {
            'details': {
                'profile_pic': {
                    'status': 1 if bool(details_object.profile_file) else 0,
                    'url': details_object.profile_file.url if bool(details_object.profile_file) else '',
                }
            },
            'designation': {
                'teacher': str(designation_object.teacher.id),
                'id': str(designation_object.id),
                'designation': designation_object.designation if designation_object.designation is not None else '',
                'department': designation_object.department if designation_object.department is not None else '',
                'institute': designation_object.institute if designation_object.institute is not None else '',
            },
            'publications_book': publications_book,
            'publications_journal': publications_journal,
            'publications_paper': publications_paper,
            'sttps': sttps,
            'workshops': workshops,
            'oiis': oiis,
            'consultancys': consultancys,
            'awards': awards,
            'projects': projects,
            'ecas': ecas,
        }
        return render(request, "Dashboard/activity.html", {'data': data})
    return redirect('/')


def profile_pic(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('file')
        try:
            details = Details.objects.filter(teacher__teacher=request.user).get()
            details.profile_file = profile_pic
            details.save()
        except:
            return JsonResponse({'status': False})

        return JsonResponse({'status': True})

    return JsonResponse({'status': False})

