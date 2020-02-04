from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('contact/',views.ContactPage.as_view(),name='contact'),
    path('contactform/',views.ContactFormPage.as_view(),name='contactform'),
]
