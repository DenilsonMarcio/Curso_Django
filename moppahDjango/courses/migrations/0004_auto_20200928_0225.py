# Generated by Django 3.1.1 on 2020-09-28 05:25

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200928_0212'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='enrollment',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
