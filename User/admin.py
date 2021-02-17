from django.contrib import admin
from .models import *


@admin.register(CollegeStudentData)
class CollegeStudentDataAdmin(admin.ModelAdmin):
    list_display = ('prn', 'first_name', 'last_name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student',)
