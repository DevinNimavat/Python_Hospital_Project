# Generated by Django 4.2.16 on 2024-11-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0011_alter_registerdata_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('msg', models.TextField()),
            ],
        ),
    ]
