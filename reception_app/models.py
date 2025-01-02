from django.db import models

from userapp.models import appointment_data

# Create your models here.

appointment_data()


class add_patient_data(models.Model):
    objects = None
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address = models.TextField()
    mobile = models.BigIntegerField()
    test_name = models.CharField(max_length=50)
    test_date = models.DateField()
    test_result = models.TextField()
    remark = models.TextField()
    crp = models.IntegerField()
    wbc = models.IntegerField()
    hemoglobin = models.IntegerField()
    platelet = models.IntegerField()
    blood_glucose = models.FloatField()
    bilirubin = models.IntegerField()
    sodium = models.IntegerField()
    potassium = models.IntegerField()


class invoice_data(models.Model):
    DoesNotExist = None
    objects = None
    created = models.DateTimeField(auto_now_add=True)
    patient_name = models.CharField(max_length=50)
    patient_id = models.IntegerField()
    dob = models.DateField()
    admission_date = models.DateField()
    discharge_date = models.DateField()
    room_charge = models.IntegerField()
    doctor_charge = models.IntegerField()
    laboratory_charge = models.IntegerField()
    medication = models.IntegerField()
    total_amount = models.IntegerField()

    def save(self, *args, **kwargs):
        # Automatically calculate the total amount when saving
        self.total_amount = self.room_charge + self.doctor_charge + self.laboratory_charge + self.medication
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient_name} - {self.patient_id}"
