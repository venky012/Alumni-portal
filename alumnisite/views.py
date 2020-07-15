from django.shortcuts import render
from django.views.generic import TemplateView
# from ase-1-site.accounts.models import User
# from ase-1-site.accounts.filters import UserFilter


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

# class SearchPage(TemplateView):
#     template_name='search_mail.html'

#class JobsPage(TemplateView):
 #   template_name='jobs.html'

class NewsroomPage(TemplateView):
    template_name='newsroom.html'


def handler404(request,exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

# def SearchPage(request, username):
#     get_user = User.objects.all()
#     context = {
#        "get_user": get_user
#     }


#     return render(request, 'search_mail.html', context)