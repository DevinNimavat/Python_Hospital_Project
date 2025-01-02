from django import forms
from .models import *

class appointment_form(forms.ModelForm):
    class Meta:
        model=appointment_data
        fields=['name','email','department','appointment_date','appointment_time','state','city','address','mobile','symptoms','medical_history']

class add_patient_form(forms.ModelForm):
    class Meta:
        model=add_patient_data
        fields=['firstname','lastname','age','gender','address','mobile','test_name','test_date','test_result','remark','crp','wbc','hemoglobin','platelet','blood_glucose','bilirubin','sodium','potassium']

class invoice_form(forms.ModelForm):
    class Meta:
        model=invoice_data
        fields='__all__'