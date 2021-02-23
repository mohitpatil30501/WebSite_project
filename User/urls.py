from django.urls import path
from . import views

urlpatterns = [
    path('login', views.auth_login, name='student_login'),
    path('logout', views.auth_logout, name='student_logout'),
    path('signup', views.auth_signup, name='student_signup'),
    path('signup/student', views.student_create, name='student_create'),
    path('signup/teacher', views.teacher_create, name='teacher_create'),

    path('email_verification/student/<str:username>/<str:data>', views.email_verification_of_student, name='student_email_verification_student'),
    path('email_verification/teacher/<str:username>/<str:data>', views.email_verification_of_teacher, name='student_email_verification_teacher'),
    # path('signup/teacher', views.teacher_create, name='teacher_create'),

    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('reset_password/<str:username>/<str:data>', views.reset_password_get, name='reset_password_get'),
    path('reset_password', views.reset_password_post, name='reset_password_post'),
]
