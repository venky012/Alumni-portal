from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('events/',views.EventsPage.as_view(),name='events'),
    path('gallery/',views.GalleryPage.as_view(),name='gallery'),
    path('profile_page/',views.ProfilePage,name='profile_page'),
    path('queries/',views.queriesList,name="queries_list"),
]
