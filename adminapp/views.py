from django.shortcuts import render, redirect
from django.contrib.auth import logout
from adminapp.forms import doctor_form, doctor_update_form, add_staff_form, staff_update_form
from adminapp.models import doctor_register, add_staff_data
from reception_app.models import add_patient_data
from userapp.views import admin_login
from userapp.models import appointment_data
from reception_app.models import add_patient_data
from .models import *
# Create your views here.

def admin_dashbord(requets):
    admin_user=requets.session.get('admin_user')
    print(admin_user)
    return render(requets, 'Admin_side/admin-dashbord.html',{'user':admin_user})

def add_doctor(request):
    msg=''
    if request.method=='POST':
        new=doctor_form(request.POST,request.FILES)
        if new.is_valid():
            new.save()
            print('Doctor add SuccessFully..')
            msg='Doctor add SuccessFully..'
            return redirect('show_doctor')
        else:
            print(new.errors)
            msg='Some Thing Want Wrong.... Try Again....'
    return render(request,'Admin_side/add_doctor.html',{'msg':msg})

def show_doctor(request):
    data=doctor_register.objects.all()
    return render(request,'Admin_side/show_doctor.html',{'data':data})

def show_appointment(request):
    data=appointment_data.objects.all()
    return render(request,'Admin_side/show_appointment.html',{'data':data})

def delete_doctor(request,id):
    doc=doctor_register.objects.get(id=id)
    doctor_register.delete(doc)
    return redirect('show_doctor')

def update_doctor(request,id):
    docid=doctor_register.objects.get(id=id)
    if request.method=='POST':
        doc=doctor_update_form(request.POST,instance=docid)
        if doc.is_valid():
            doc.save()
            print('Record Update Successfully')
            return redirect('show_doctor')
        else:
            print(doc.errors)
    return render(request,'Admin_side/update_doctor.html',{'docid':docid})

def update_staff(request,id):
    sta_id=add_staff_data.objects.get(id=id)
    if request.method=='POST':
        sta=staff_update_form(request.POST,instance=sta_id)
        if sta.is_valid():
            sta.save()
            print('Record Update SuccessFully')
            return redirect('show_staff')
        else:
            print(sta.errors)
    return render(request,'Admin_side/update_staff.html',{'sta_id':sta_id})
def add_staff(request):
    msg=''
    if request.method=='POST':
        staff=add_staff_form(request.POST,request.FILES)
        if staff.is_valid():
            staff.save()
            print('Staff Added SuccessFully..')
        else:
            print(staff.errors)
    return render(request,'Admin_side/add_staff.html')

def show_staff(request):
    staff_data=add_staff_data.objects.all()
    return render(request,'Admin_side/show_staff.html',{'staff_data':staff_data})


def show_patients_data(request):
    patients_data=add_patient_data.objects.all()
    return render(request,'Admin_side/show_patients.html',{'patients_data':patients_data})

def delete_staff(request,id):
    sta=add_staff_data.objects.get(id=id)
    add_staff_data.delete(sta)
    return redirect('show_staff')

def delete_appointment(request,id):
    appoint=appointment_data.objects.get(id=id)
    appointment_data.delete(appoint)
    return redirect('show_appointment')