from django.contrib import admin
from django.urls import path, include
from reception_app import  views

urlpatterns=[
    path('reception_dashbord/',views.reception_dashbord,name='reception_dashbord'),
    path('appointments/',views.appointments),
    path('add_appointment/',views.add_appointment),
    path('doctor/',views.doctor),
    path('invoice/',views.invoice),
    path('patient/',views.patient),
    path('new_patient/',views.patient),
    path('add_new_patient/',views.add_new_patient),
    path('invoice_pdf/<int:bill_id>/',views.invoice_pdf,name='invoice_pdf')

]