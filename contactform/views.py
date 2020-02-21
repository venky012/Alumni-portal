from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm
import requests
# for contact form queries
from contactform.models import ContactForm_queries

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            
            ''' code for recaptcha verification '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            if result['success']:
                name = form.cleaned_data['name']
                subject = form.cleaned_data['subject']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                try:
                    contactformqueries = ContactForm_queries.objects.get_or_create(name=name,email=email,subject=subject,message=message)
                    send_mail('New Enquiry : '+subject,'From : '+name+'\n'+message, email, ['poojariv53@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('success')
            else:
                form.add_error(None, "invalid captcha")

    return render(request, "contactform.html", {'form': form})

def successView(request):
    return render(request,'thanks_for_message.html')