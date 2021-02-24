import uuid

from django.db import models
from User.models import *


# Details Page
class Details(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    id = models.UUIDField(default=uuid.uuid4(), unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=200, blank=True, null=True, default=None)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, blank=True, null=True, default=None)
    mobile = models.CharField(max_length=10, blank=True, null=True, default=None)
    address = models.CharField(max_length=500, blank=True, null=True, default=None)
    date_of_birth = models.CharField(max_length=10, blank=True, null=True, default=None)


# Designation Page
class Designation(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True, primary_key=True)

    designation = models.CharField(max_length=100, blank=True, null=True, default=None)
    department = models.CharField(max_length=100, blank=True, null=True, default=None)
    institute = models.CharField(max_length=200, blank=True, null=True, default=None)


class SubjectOfInterest(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True, primary_key=True)

    subject_of_interest = models.CharField(max_length=100)


# class Academics(models.Model):
#     pass
#
#
# class ProfessionalMembership(models.Model):
#     pass
#
#
# class TeachingExperience(models.Model):
#     pass
#
#
# class AdministrativeExperience(models.Model):
#     pass
#
#
# class IndustrialExperience(models.Model):
#     pass
#
#
# class FacultyDevelopment(models.Model):
#     pass
