# Generated by Django 4.2.16 on 2024-10-29 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_alter_registerdata_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdata',
            name='image',
            field=models.ImageField(upload_to='Image/Patient Image/'),
        ),
    ]
