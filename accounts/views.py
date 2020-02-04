from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User

from django.views.generic import TemplateView
from .forms import RegistrationForm
from .tokens import account_activation_token
import re

EMAIL_REGEX = re.compile(r'([A-Za-z])\w+.([a-z0-9])\w+@iiits.in')


# def validateEmail(email):
#     if len(email) > 13 :
#         if re.match('\b([A-Za-z])\w+.([a-z0-9])\w+@iiits.in\b', email) != None:
#             return 1
#     return 0

def accounts_register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            if EMAIL_REGEX.match(request.POST['email']):
                user = registerForm.save(commit=False)
                user.email = registerForm.cleaned_data['email']
                user.set_password(registerForm.cleaned_data['password'])
                user.is_active = False
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
                return HttpResponse('registered succesfully and activateion sent')   
    else:
        registerForm = RegistrationForm()
    return render(request, 'accounts/register.html',{'form': registerForm})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError,User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('login')
    else:
        return render(request, 'accounts/account_activation_invalid.html')



