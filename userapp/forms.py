from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordResetForm
from .models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['firstname','lastname','email','mobile','state','city','dob','password1','password2','image']

class register_form(forms.ModelForm):
    class Meta:
        model=appointment_data
        fields=['name','email','department','appointment_date','appointment_time','state','city','address','mobile','symptoms','medical_history']

class profile_form(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['firstname','lastname','mobile','state','city','dob','image']

class contact_form(forms.ModelForm):
    class Meta:
        model=contact_data
        fields=['name','email','msg']

class CustomPasswordReset(PasswordResetForm):
    class Meta:
        model=CustomUser
        fields=['email']

class review_form(forms.ModelForm):
    class Meta:
        model=doctor_review
        fields=['doctor_name','your_name','your_email','rating','comment']