import random

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from weasyprint import HTML
from reception_app.forms import appointment_form, add_patient_form, invoice_form
from reception_app.models import add_patient_data, invoice_data
from userapp.models import appointment_data


# Create your views here.

def reception_dashbord(request):
    user = request.session.get('user')
    return render(request, 'Reception_side/reception-dashbord.html', {'user': user})


def appointments(request):
    user = request.session.get('user')
    data = appointment_data.objects.all()
    return render(request, 'Reception_side/appointments.html', {'user': user, 'data': data})


def add_appointment(request):
    apidata = get_api()
    user = request.session.get('user')
    if request.method == 'POST':
        data = appointment_form(request.POST)
        if data.is_valid():
            data.save()
            print('Data Save...')
        else:
            print(data.errors)
    return render(request, 'Reception_side/add_appointment.html', {'user': user, 'apidata': apidata})




def invoice(request):
    pid=random.randint(100000,999999)
    if request.method == 'POST':
        form = invoice_form(request.POST)
        if form.is_valid():
            invoice = form.save()
            return redirect('invoice_pdf', bill_id=invoice.id)
    else:
        form = invoice_form()
    return render(request, 'Reception_side/invoice.html', {'form': form,'pid':pid})

def invoice_pdf(request, bill_id):
    invoice = invoice_data.objects.get(id=bill_id)
    if request.method == 'POST':
        # Generate PDF
        html_string = render_to_string('Reception_side/invoice_template.html', {'invoice': invoice})
        html = HTML(string=html_string)
        pdf = html.write_pdf()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.patient_id}.pdf"'
        return response
    return render(request, 'Reception_side/invoice_pdf.html', {'invoice': invoice})

def patient(request):
    user = request.session.get('user')
    data = add_patient_data.objects.all()
    return render(request, 'Reception_side/patient.html', {'user': user, 'data': data})


def doctor(request):
    user = request.session.get('user')
    return render(request, 'Reception_side/doctor.html', {'user': user})


def get_api():
    url = 'https://raw.githubusercontent.com/sab99r/Indian-States-And-Districts/refs/heads/master/states-and-districts.json'
    req = requests.get(url)
    data = req.json()
    state = data['states']

    return state


def add_new_patient(request):
    msg = ''
    if request.method == 'POST':
        patient = add_patient_form(request.POST)
        if patient.is_valid():
            patient.save()
            print('Patient Added Successfully...')
            msg = 'Patient Added Successfully...'
        else:
            print(patient.errors)
            msg = 'Something Went Wrong...  Try Again...'
    return render(request, 'Reception_side/add_new_patient.html', {'msg': msg})


# def invoice_pdf(request):
#     return render(request, 'Reception_side/invoice_pdf.html')
