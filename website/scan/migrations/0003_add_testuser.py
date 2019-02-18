# Generated by Django 2.1.7 on 2019-02-18 19:25
import os

from django.db import migrations

from login.models import DoctorUser


def add_docy_users(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return

    # Creates a docy/docy superuser (used for testing!)
    u_name = 'docy'
    u_email = 'noreply@docy.demo'
    u_pass = 'docy'

    DoctorUser.objects.create_superuser(u_name, u_email, u_pass)

class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0002_auto_20190218_2025'),
    ]

    operations = [
        migrations.RunPython(add_docy_users),
    ]