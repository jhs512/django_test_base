# Generated by Django 4.0 on 2022-01-03 11:22

from django.db import migrations

from accounts.models import User


def gen_data(apps, schema_editor):
    User.objects.create_superuser(username='admin', password='1234')


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('accounts', '0003_user_gender'),
    ]

    operations = [
        migrations.RunPython(gen_data),
    ]
