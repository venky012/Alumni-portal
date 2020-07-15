# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
import os

def update_filename(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]
    if instance.username:
        filename = '{}.{}'.format(instance.username, ext)
    return os.path.join(upload_to, filename)

# Create your models here.
class User(AbstractUser):
    """
    Extended from Abstract User
    List of inherited fields: first_name, last_name, email, username, password
    """
    phone_number = models.CharField(
        max_length=15,
        blank = False,
        default="",
        validators=[
            RegexValidator(
                regex='^([+][0-9]{1,4}[6-9][0-9]{9})$',
                message='mobile number should be in the format "+999999999" ',
                code='invalid_phone_number'
            ),
        ]
    )
    
    email_confirmed = models.BooleanField(default=False)
    conditions = models.BooleanField(default=False)
    
    avatar = models.ImageField(upload_to=update_filename,blank = True)
    linkedin_url = models.URLField(blank = True)
    github_url = models.URLField(blank = True)
    webpage_url = models.URLField(blank = True)
    passout_year = models.CharField(max_length=4,blank=True)
    company = models.CharField(max_length=100,blank = True)
    summary = models.CharField(max_length=100,blank = True)
    place = models.CharField(max_length = 100,blank = True)


class linkedin_model(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    skills = models.TextField(blank=True)
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    currentLocation = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username
