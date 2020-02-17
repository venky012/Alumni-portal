from django.contrib import admin
from django.urls import path
from .views import emailView, successView

urlpatterns = [
    path('contactform/', emailView, name='contactform'),
    path('success/', successView, name='success'),
]