# Generated by Django 3.2.18 on 2023-05-02 21:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]
