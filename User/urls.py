from django.urls import path
from . import views

urlpatterns = [
    path('check/login', views.check_login),
    path('login', views.auth_login, name='student_login'),


    path('login', views.auth_login, name='student_login'),
    path('logout', views.auth_logout, name='student_logout'),
    path('signup', views.auth_signup, name='student_signup'),
    path('signup/student', views.student_create, name='student_create'),
    path('signup/student/email_verification/<str:username>/<str:data>', views.email_verifcation_of_student, name='student_email_verification'),
    # path('signup/teacher', views.teacher_create, name='teacher_create'),
]
