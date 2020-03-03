from django.shortcuts import render
from django.views.generic import TemplateView
from contactform.models import ContactForm_queries

# from django.contrib.auth.decorators import login_required
# from accounts.decorators import email_confirmation_required

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

class EventsPage(TemplateView):
    template_name = 'events.html'

class GalleryPage(TemplateView):
    template_name='gallery.html'

class TimelinePage(TemplateView):
    template_name='timeline.html'

class JobsPage(TemplateView):
    template_name='jobs.html'

class NewsroomPage(TemplateView):
    template_name='newsroom.html'


