from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(appointment_data)
admin.site.register(doctor_review)
