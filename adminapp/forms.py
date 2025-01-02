from django import forms
from .models import *

class doctor_form(forms.ModelForm):
    class Meta:
        model=doctor_register
        fields='__all__'

class doctor_update_form(forms.ModelForm):
    class Meta:
        model=doctor_register
        fields=['name','email','mobile','dob','specialization','address','year_of_experienc','gender','degree','profile_image']

class add_staff_form(forms.ModelForm):
    class Meta:
        model=add_staff_data
        fields='__all__'

class staff_update_form(forms.ModelForm):
    class Meta:
        model=add_staff_data
        fields=['name','email','mobile','blood_group','staff_type','staff_department','state','city','education','image']