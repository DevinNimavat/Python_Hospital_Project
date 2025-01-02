from django.db import models

# Create your models here.

class doctor_register(models.Model):
    objects = None
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    dob=models.DateField()
    specialization=models.CharField(max_length=50)
    address=models.TextField()
    year_of_experienc=models.IntegerField()
    gender=models.CharField(max_length=20)
    degree=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='Media/Doctor Image/')

class add_staff_data(models.Model):
    objects = None
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    blood_group=models.CharField(max_length=10)
    staff_type=models.CharField(max_length=100)
    staff_department=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    education=models.CharField(max_length=100)
    image=models.FileField(upload_to='Media/Staff Image/')
    

