from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import login
from accounts.models import User
from accounts.tokens import account_activation_token
from django.contrib import messages
import requests


def email_confirmation_required(function):
    """
    A decorator which allows to access route only if email for current user has been confirmed.
    THE DECORATOR login_required MUST ALWAYS PRECEDE THIS.
    i.e. ensure that user is logged on before this decorator is called
    """

    def checker(request, *args, **kwargs):
        user=request.user
        if request.user.is_staff is True:
            return function(request, *args, **kwargs)
        elif request.user.email_confirmed is True:
            return function(request, *args, **kwargs)
        else:
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
            messages.success(request, ' Check your email for activation link')
            return render(request, 'accounts/email_activation_required.html')

        # Add the confirmation route above

    return checker

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError,User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        # user.is_active = True
        user.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('login')
    else:
        return render(request, 'accounts/account_activation_invalid.html')