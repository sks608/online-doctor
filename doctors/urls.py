from django.urls import path
from .views import hospital_list, doctor_list

urlpatterns = [

    path(
        'hospital-list/',
        hospital_list,
        name='hospital_list'
    ),

    path(
        'doctor-list/',
        doctor_list,
        name='doctor_list'
    ),

]