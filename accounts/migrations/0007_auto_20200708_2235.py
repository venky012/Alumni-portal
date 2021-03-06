# Generated by Django 2.2.10 on 2020-07-08 17:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passout_year',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
