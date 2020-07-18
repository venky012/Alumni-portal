from django.urls import path
from . import views

urlpatterns = [
    path('donateus/', views.donateus, name='donation-page'),
    path('donateus/form', views.index, name="index"),
    path('donateus/charge/', views.charge, name="charge"),
    path('donateus/success/<str:args>/', views.successMsg, name="success"),
]
