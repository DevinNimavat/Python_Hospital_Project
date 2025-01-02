from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.db import models


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('You Did Not Entered Valid Email Address..')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_doctor', True)
        extra_fields.setdefault('is_user', True)
        extra_fields.setdefault('is_reception', True)
        extra_fields.setdefault('is_newadmin', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    created_at = models.DateTimeField(auto_now_add=True, )
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    dob = models.DateField(blank=True, null=True)
    mobile = models.BigIntegerField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='Media/Documents/',default='/static/image/')


    is_active =models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)
    is_user=models.BooleanField(default=False)
    is_newadmin=models.BooleanField(default=False)
    is_reception=models.BooleanField(default=False)

    object=CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class appointment_data(models.Model):
    objects = None
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    department=models.CharField(max_length=20)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
    symptoms=models.TextField()
    medical_history=models.TextField()
    image=models.ImageField(upload_to='Media/Patient Image/')


class contact_data(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    msg=models.TextField()

class doctor_review(models.Model):
    objects = None
    created=models.DateTimeField(auto_now_add=True)
    doctor_name=models.CharField(max_length=50)
    your_name=models.CharField(max_length=50)
    your_email=models.EmailField()
    rating=models.CharField(max_length=20)
    comment=models.TextField()