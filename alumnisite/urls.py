from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('profile_page/',views.ProfilePage,name='profile_page'),
    path('queries/',views.queriesList,name="queries_list"),
]
