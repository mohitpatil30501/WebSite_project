from django.contrib import admin
from .models import *


@admin.register(CollegeStudentData)
class CollegeStudentDataAdmin(admin.ModelAdmin):
    list_display = ('prn', 'first_name', 'last_name',)


@admin.register(CollegeTeacherData)
class CollegeTeacherDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher',)
