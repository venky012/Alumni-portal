from django.contrib import admin
from django.urls import path,include
from . import views

handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('events/',views.EventsPage.as_view(),name='events'),
    path('gallery/',views.GalleryPage.as_view(),name='gallery'),
    path('timeline/',views.TimelinePage.as_view(),name='timeline'),
    path('newsroom/',views.NewsroomPage.as_view(),name='newsroom'),
    # path('profile_page/',views.ProfilePage,name='profile_page'),
    path('jobs/',views.JobsPage.as_view(),name='jobs'),
]


