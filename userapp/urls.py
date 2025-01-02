from tempfile import template

from django.urls import path
from userapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index),
    path('login/', views.user_login, name='login'),
    path('register/', views.register),
    path('about/', views.about),
    path('contact/', views.contact,name='contact'),
    path('patient', views.patient),
    path('admin_login/', views.admin_login),
    path('term-condition/', views.term),
    path('policy/', views.policy),
    path('doctor-login/', views.doctor_login),
    path('reception-login/', views.reception_login),
    path('doctor_profile/', views.doctor_profile),
    path('appointment/', views.appointment),
    path('appointment_list/', views.appointment_list, name='appointment_list'),
    path('user_logout/', views.user_logout),
    path('otp_verification/', views.otp_verify, name='otp_verify'),
    path('admin-logout/', views.admin_logout),
    path('doctor-logout/', views.doctor_logout),
    path('update_profile/',views.update_profile),
    path('reception_logout/',views.reception_logout),
    path('review/',views.review),


    path('forgot-password/',auth_views.PasswordResetView.as_view(template_name='User_side/forgot-password.html'),name='forgot-password'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='User_side/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='User_side/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='User_side/password_reset_complete.html'),name='password_reset_complete'),


]
