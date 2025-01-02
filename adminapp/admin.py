from django.contrib import admin
from adminapp.models import doctor_register, add_staff_data

# Register your models here.

admin.site.register(doctor_register)
admin.site.register(add_staff_data)