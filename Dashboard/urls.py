from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('edit/details', views.edit_details, name='edit_details'),
    path('edit/designation', views.edit_designation, name='edit_designation'),
    path('edit/activity', views.edit_activity, name='edit_activity'),
]
