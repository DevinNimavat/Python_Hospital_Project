from django.shortcuts import render
from userapp.models import appointment_data, doctor_review
from adminapp.models import add_staff_data




# Create your views here.

def doctor_dashbord(request):
    doctor_user = request.session.get('doctor_user')
    print(doctor_user)
    data = appointment_data.objects.all()
    return render(request, 'Doctor_side/doctor-dashbord.html', {'user': doctor_user,'data':data})

def my_hospital_staff(request):
    staff_data=add_staff_data.objects.all()
    return render(request,'Doctor_side/my-hospital-staff.html',{'staff_data':staff_data})

def doctor_patients_reviews(request):
    doc_riv=doctor_review.objects.all()
    return render(request,'Doctor_side/doctor_review.html',{'doc_riv':doc_riv})

