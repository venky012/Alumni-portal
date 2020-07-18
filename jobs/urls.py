from django.contrib import admin
from django.urls import path
from .views import PostJobView
from .views import JobsView,DeleteJob

urlpatterns = [
    path('post_job/', PostJobView, name='post_job'),
    path('delete_job/<int:id>', DeleteJob, name='delete_job'),
    path('jobs/',JobsView,name="jobs"),
]