from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm, ReplyForm
import requests
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# for contact form queries
from contactform.models import ContactForm_queries, ReplyForm_queries
from django.views.decorators.cache import cache_control


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

# @login_required
# def queriesList(request):  
#     queries_list = ContactForm_queries.objects.order_by('email')
#     my_queries={'queries_list':queries_list}
#     return render(request,'queries_list.html',context=my_queries)    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def queriesList(request):
    if request.method == 'GET':
        form = ReplyForm()
    else :
        form = ReplyForm(request.POST)
        if form.is_valid():
            
            query = ContactForm_queries.objects.get(id = form.cleaned_data['pid'])
    
            replymessage = form.cleaned_data['reply_message']

            try:
                replyformqueries = ReplyForm_queries.objects.get_or_create(query_user = query,reply_message = replymessage)
                send_mail('Reg : '+query.subject,'Dear Sir/Madam,\nThanks for your query.\n'+replymessage, 'poojariv53@gmail.com', [query.email])
                messages.success(request,'Message sent to user')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    
    queries_list=ContactForm_queries.objects.all()
    my_queries={'queries_list':queries_list}
    return render(request,'queries_list.html',context=my_queries)


