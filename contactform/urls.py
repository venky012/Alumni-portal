from django.contrib import admin
from django.urls import path
from .views import emailView, successView,queriesList

urlpatterns = [
    path('contactform/', emailView, name='contactform'),
    path('success/', successView, name='success'),
    path('queries/',queriesList,name="queries_list"),
]