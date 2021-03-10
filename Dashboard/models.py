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
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    subject_of_interest = models.CharField(max_length=100)


class Academics(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    degree = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    remarks = models.CharField(max_length=100)


class ProfessionalMembership(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    society = models.CharField(max_length=100)
    ist_no = models.CharField(max_length=100)
    date_of_membership = models.CharField(max_length=10)


class TeachingExperience(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_join = models.CharField(max_length=10)
    date_of_leave = models.CharField(max_length=10)


class AdministrativeExperience(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_join = models.CharField(max_length=10)
    date_of_leave = models.CharField(max_length=10)


class IndustrialExperience(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_join = models.CharField(max_length=10)
    date_of_leave = models.CharField(max_length=10)


class FacultyDevelopment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_approval = models.CharField(max_length=10)


# Activity Page
class PublicationsBook(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    year = models.CharField(max_length=100)


class PublicationsJournal(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    page = models.CharField(max_length=10)
    year = models.CharField(max_length=5)
    url = models.CharField(max_length=300)
    level = models.CharField(max_length=15)


class PublicationsPaper(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    year = models.CharField(max_length=5)
    url = models.CharField(max_length=300)
    level = models.CharField(max_length=15)


class ShortTermsTrainingProgram(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    year = models.CharField(max_length=5)
    date_form = models.CharField(max_length=10)
    date_to = models.CharField(max_length=10)
    day = models.IntegerField()


class Workshops(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    year = models.CharField(max_length=5)
    date_form = models.CharField(max_length=10)
    date_to = models.CharField(max_length=10)
    day = models.IntegerField()


class OtherInstituteInteractions(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    organization = models.CharField(max_length=100)
    year = models.CharField(max_length=5)
    invitee = models.CharField(max_length=20)


class Consultancy(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    organization = models.CharField(max_length=100)
    year = models.CharField(max_length=5)
    work_done = models.CharField(max_length=300)
    cost = models.CharField(max_length=20)


class AwardReceived(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    organization = models.CharField(max_length=100)
    year = models.CharField(max_length=5)
    title = models.CharField(max_length=100)


class ProjectGuided(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    year = models.CharField(max_length=5)
    level = models.CharField(max_length=3)


class ExtraCurricularActivities(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), unique=True)
    index = models.AutoField(primary_key=True)

    name = models.CharField(max_length=200)
    year = models.CharField(max_length=5)
