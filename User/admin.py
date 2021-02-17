from django.contrib import admin
from .models import *


@admin.register(CollegeStudentData)
class CollegeStudentDataAdmin(admin.ModelAdmin):
    list_display = ('prn', 'first_name', 'last_name',)
