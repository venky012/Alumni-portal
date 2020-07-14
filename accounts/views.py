from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import login
from accounts.models import User
from jobs.models import Jobs_details

from django.views.generic import TemplateView
from .forms import RegistrationForm
from .tokens import account_activation_token
import re
import time
from django.contrib import messages
import requests
from django.contrib.auth.decorators import login_required
from accounts.decorators import email_confirmation_required
from django.views.decorators.cache import cache_control

from .filters import UserFilter 

EMAIL_REGEX = re.compile(r'([A-Za-z])\w+.([a-z0-9])\w+@iiits.in')

MOBILE_REGEX = re.compile(r'^([+][0-9]{1,4}[6-9][0-9]{9})$')


def accounts_register(request):
    if request.method == "GET":
        p = request.GET.copy()
        if 'username' in p:
            name = p['username']

            if len(name) == 0:
                return HttpResponse(0)
            else:
                if User.objects.filter(username__iexact=name):
                    return HttpResponse(False)
                else:
                    return HttpResponse(True)

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST or None)
        if registerForm.is_valid():
            if EMAIL_REGEX.match(request.POST['email']):

                ''' code for recaptcha verification '''
                recaptcha_response = request.POST.get('g-recaptcha-response')
                data = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                r = requests.post(
                    'https://www.google.com/recaptcha/api/siteverify', data=data)
                result = r.json()
                ''' End reCAPTCHA validation '''
                if result['success']:
                    user = registerForm.save(commit=False)
                    user.email = registerForm.cleaned_data['email']
                    user.set_password(registerForm.cleaned_data['password'])
                    user.phone_number = registerForm.cleaned_data['phone_number']
                    user.linkedin_url = registerForm.cleaned_data['linkedin_url']
                    user.github_url = registerForm.cleaned_data['github_url']
                    user.webpage_url = registerForm.cleaned_data['webpage_url']
                    user.company = registerForm.cleaned_data['company']
                    user.place = registerForm.cleaned_data['place']
                    user.summary = registerForm.cleaned_data['summary']
                    user.passout_year = registerForm.cleaned_data['passout_year']
                    user.conditions = registerForm.cleaned_data['conditions']
                    # Save the User object
                    user.save()

                    # get current site
                    current_site = get_current_site(request)
                    subject = 'Activate your Account'
                    # create Message
                    message = render_to_string('accounts/account_activation_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                    })
                    # send activation link to the user
                    user.email_user(subject=subject, message=message)
                    return render(request, 'accounts/account_activation_sent.html')
                else:
                    registerForm.add_error(None, "invalid captcha")
            else:
                registerForm.add_error(None, 'Use IIITS mail only')

    else:
        registerForm = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': registerForm})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        # user.is_active = True
        user.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'accounts/account_activation_invalid.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
@email_confirmation_required
def user_profile(request, username):
    get_user = User.objects.get(username=username)
    jobslist = Jobs_details.objects.filter(user__username=username)
    context = {
        "get_user": get_user,
        "jobslist": jobslist
    }


    return render(request, 'profile_page.html', context)


def SearchPage(request):
    get_user = User.objects.filter(is_staff=False)
    myFilter = UserFilter(request.GET,queryset=get_user)
    context = {
       "get_user": get_user,
       "myFilter": myFilter

    }
    if "sendMail" in request.GET:
        queryDict = request.GET.copy()
        mailList = []
        for i in queryDict.keys():
            if queryDict[i] == "on":
                mailList.append(i)
        print(mailList)
    return render(request, 'search_mail.html', context)
