# Generated by Django 4.0 on 2022-01-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_gen_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', '남성'), ('W', '여성')], max_length=1, verbose_name='성별'),
        ),
    ]
