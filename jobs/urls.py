from django.contrib import admin
from django.urls import path
from .views import PostJobView

urlpatterns = [
    path('post_job/', PostJobView, name='post_job'),
]