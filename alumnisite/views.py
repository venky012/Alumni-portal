from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

class ContactFormPage(TemplateView):
    template_name = 'contactform.html'

class ContactPage(TemplateView):
    template_name = 'contact.html'

