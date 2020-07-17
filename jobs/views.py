from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required
from accounts.decorators import email_confirmation_required
from .forms import PostJobForm
from accounts.models import User
from .models import Jobs_details
from django.views.decorators.cache import cache_control
import random


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@email_confirmation_required
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
            job.job_title=form.cleaned_data['job_title']
            job.category=form.cleaned_data['category']
            job.imgSrc="assets/jobs_images/img"+str(random.choice([i for i in range(1,8)]))+".jpg"
            job.save()
            return redirect('/jobs/')
            
            
    return render(request, "post_job.html", {'form': form})

def JobsView(request):
    jobslist=Jobs_details.objects.all()
    return render(request,'jobs.html',{"jobslist":jobslist})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@email_confirmation_required
@login_required
def DeleteJob(request,id):
    obj = Jobs_details.objects.get(id=id)
    if obj:
        obj.delete()
    return redirect('/profile_page/userinfo/'+str(request.user.username)+'/')