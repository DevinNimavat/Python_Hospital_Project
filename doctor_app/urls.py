from django.contrib import admin
from django.urls import path, include
from doctor_app import  views

urlpatterns=[
    path('doctor-dashbord/',views.doctor_dashbord,name='doctor-dashbord'),
    path('my_hospital_staff/',views.my_hospital_staff),
    path('doctor_reviews/',views.doctor_patients_reviews),
]