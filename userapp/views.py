import random

import requests
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from Hospital_Project import settings
from .forms import CustomUserCreationForm, register_form, profile_form, contact_form, review_form
from .models import *


# from requests import session


# Create your views here.

def index(request):
    user = request.session.get('email')
    return render(request, 'User_side/index.html', {'user': user})


def user_login(request):
    msg = ''
    if request.method == 'POST':
        em = request.POST['email']
        pas = request.POST['password']
        userid = CustomUser.object.get(email=em)
        user = authenticate(request, email=em, password=pas)
        if user:
            login(request, user)
            print('Login Success')
            msg = 'Login Success'
            request.session['email'] = em
            request.session['userid'] = userid.id
            return redirect('/')
        else:
            print('Login Failed')
            msg = 'Login Failed'
    return render(request, 'User_side/login.html', {'msg': msg})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():

            # Send Mail

            global otp
            otp = random.randint(111111, 999999)
            print(otp)
            fnm = request.POST['firstname']
            lnm = request.POST['lastname']
            sub = 'OTP'
            msg = f'Welcome {fnm} {lnm}.Thank You for register. Your Registration Success.\n\n your otp is:{otp}'
            from_id = settings.EMAIL_HOST_USER
            to = [request.POST['email']]

            send_mail(subject=sub, message=msg, from_email=from_id, recipient_list=to)
            form.save()
            print('Data Saved')
            return redirect('otp_verify')
        else:
            print(form.errors)
    return render(request, 'User_side/register.html')


def about(request):
    user = request.session.get('email')
    return render(request, 'User_side/about.html', {'user': user})


def contact(request):
    user = request.session.get('email')
    msg = ''
    if request.method == 'POST':
        data = contact_form(request.POST)
        if data.is_valid():
            data.save()
            print('Message Send Successfully..')
            msg = 'Message Send Successfully..'
            return redirect('contact')
        else:
            print(data.errors)
            msg = 'Something went wrong... Tyr Again'
    return render(request, 'User_side/contact.html', {'user': user, 'msg': msg})


def patient(request):
    user = request.session.get('email')
    return render(request, 'User_side/patient.html', {'user': user})


def admin_login(request):
    msg = ''
    if request.method == 'POST':
        em = request.POST['email']
        pas = request.POST['password']

        admin_user = authenticate(request, email=em, password=pas)
        if admin_user is not None and admin_user.is_superuser and admin_user.is_newadmin:
            login(request, admin_user)
            print('Login')
            request.session['admin_user'] = em
            return redirect('admin_dashbord')
        else:
            print('Field')
    return render(request, 'Admin_side/admin_login.html', {'msg': msg})


def term(request):
    user = request.session.get('email')
    return render(request, 'User_side/terms-condition.html', {'user': user})


def policy(request):
    user=request.session.get('email')
    return render(request, 'User_side/policy.html',{'user':user})


def forgot(request):
    # if request.method=='POST':
    #     em=request.POST['email']
    #     uem=CustomUser.object.get(email=em)
    #     request.session['uid']=uem.id
    #     return redirect('reset_password')

    return render(request, 'User_side/forgot-password.html')


def doctor_login(request):
    msg = ''
    if request.method == 'POST':
        em = request.POST['email']
        pas = request.POST['password']

        doctor_user = authenticate(request, email=em, password=pas)
        # if admin_user is not None and admin_user.is_superuser:

        if doctor_user is not None and doctor_user.is_active and doctor_user.is_doctor:
            login(request, doctor_user)
            print('Login')
            request.session['doctor_user'] = em
            return redirect('doctor-dashbord')
        else:
            print('Filed')
    return render(request, 'Doctor_side/doctor-login.html')


def reception_login(request):
    msg = ''
    if request.method == 'POST':
        em = request.POST['email']
        pas = request.POST['password']

        reception_user = authenticate(request, email=em, password=pas)

        if reception_user is not None and reception_user.is_active and reception_user.is_reception:
            login(request, reception_user)
            print('Login')
            request.session['user'] = em
            return redirect('reception_dashbord')
        else:
            print('Login Field')
            msg = 'Login Field'
    return render(request, 'Reception_side/reception-login.html', {'msg': msg})


def doctor_profile(request):
    user = request.session.get('email')
    return render(request, 'User_side/doctor_profile.html', {'user': user})


def appointment(request):
    user = request.session.get('email')
    apidata = get_api()
    msg = ''
    if request.method == 'POST':
        data = register_form(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            print('Appointment Fixed')
            msg = 'Appointment Fixed'
            return redirect('appointment_list')
        else:
            print(data.errors)
            msg = 'Appointment Fixed Error.... Something Went Wrong Try Again'
    return render(request, 'User_side/appointment.html', {'user': user, 'apidata': apidata, 'msg': msg})


def appointment_list(request):
    user = request.session.get('email')
    data = appointment_data.objects.all()
    return render(request, 'User_side/appointment_data.html', {'user': user, 'data': data})


def user_logout(request):
    logout(request)
    return redirect('login')


def admin_logout(request):
    logout(request)
    return redirect('/')


def doctor_logout(request):
    logout(request)
    return redirect('/')


def reception_logout(request):
    logout(request)
    return redirect('/')


def otp_verify(request):
    global otp
    if request.method == 'POST':
        if request.POST['otp'] == str(otp):
            print('OTP Verification Success')
            return redirect('login')
        else:
            print('OTP Verification Failed')
    return render(request, 'User_side/otp_verification.html')


def get_api():
    url = 'https://raw.githubusercontent.com/sab99r/Indian-States-And-Districts/refs/heads/master/states-and-districts.json'
    req = requests.get(url)
    data = req.json()
    state = data['states']

    return state


def doctor_dashbord(request):
    user = request.session.get('email')
    return render(request, 'Doctor_side/doctor-dashbord.html', {'user': user})


def update_profile(request):
    msg = ''
    user = request.session.get('email')
    userid = request.session.get('userid')
    uid = CustomUser.object.get(id=userid)
    if request.method == 'POST':
        update = profile_form(request.POST, request.FILES)
        if update.is_valid():
            update = profile_form(request.POST, instance=uid)
            update.save()
            print('Profile Updated SuccessFully...')
            msg = 'Profile Updated SuccessFully...'

            # Email

            fnm = request.POST['firstname']
            lnm = request.POST['lastname']
            sub = 'Hospital Management System'
            msg = f'Hello Mr/Mis. {fnm} {lnm}. Your Profile Has Been Updated. \n\n Thank You.'
            from_id = settings.EMAIL_HOST_USER
            to_id = [request.POST['email']]

            send_mail(subject=sub, message=msg, from_email=from_id, recipient_list=to_id)
            return redirect('/')
        else:
            print(update.errors)
            msg = 'Profile Has Not Update... Something Went Wrong... Try Again...'
    return render(request, 'User_side/update_profile.html', {'user': user, 'uid': uid, 'msg': msg})

def review(request):
    msg=''
    user=request.session.get('email')
    if request.method=='POST':
        review=review_form(request.POST)
        if review.is_valid():
            review.save()
            print('Review is Submitted')
            msg='Review is Submitted'
        else:
            print(review.errors)
            msg='Somethings Went Wrong...  Try Again.....'
    return render(request,'User_side/review.html',{'msg':msg,'user':user})