from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required
from .forms import PostJobForm
from accounts.models import User
from .models import Jobs_details

@login_required
def PostJobView(request):
    if request.method == 'GET':
        form = PostJobForm()
    else:
        form = PostJobForm(request.POST)
        if form.is_valid():
            job = Jobs_details()
            user_obj = User.objects.get(username=request.user)
            job.user = user_obj
            job.last_date = form.cleaned_data['last_date']
            job.company = form.cleaned_data['company']
            job.place = form.cleaned_data['place']
            job.experience = form.cleaned_data['experience']
            job.salary = form.cleaned_data['salary']
            job.save()
            
            
    return render(request, "post_job.html", {'form': form})