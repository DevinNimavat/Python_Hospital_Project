# Generated by Django 4.2.16 on 2024-11-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_register',
            name='profile_image',
            field=models.ImageField(upload_to='Image/Doctor Image/'),
        ),
    ]
