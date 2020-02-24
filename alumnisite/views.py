from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from contactform.models import ContactForm_queries

from accounts.decorators import email_confirmation_required

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
    
@login_required
@email_confirmation_required
def ProfilePage(request):
    return render(request,'profile_page.html')

@login_required
def queriesList(request):
    queries_list=ContactForm_queries.objects.order_by('email')
    my_queries={'queries_list':queries_list}
    return render(request,'queries_list.html',context=my_queries)