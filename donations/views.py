from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import DonatorInfo

from django.conf import settings

import stripe
stripe.api_key = "sk_test_51GwRq2I7M5l47LQTANTu4qmSu5hi6FBlXfcKJiEvhbHjnAbyYgzMFBTGvGCDgYNpRVwx5qYG1e7aRjMaF4Qp0pWS00L3SVg6AB"


def donateus(request):
    context = {
        'donators': DonatorInfo.objects.all(),
        'amount_raised': int(DonatorInfo.objects.last().total_amount if DonatorInfo.objects.last() else 5647)
    }

    return render(request, 'donations/donations.html', context)


def index(request):
    return render(request, 'donations/index.html')


def charge(request):
    amount = int(request.POST['amount'])

    if request.method == 'POST':

        donator_temp = DonatorInfo(donator_name=request.POST['nickname'],
                                   amount=request.POST['amount'],
                                   description=request.POST['desciption'],
                                   total_amount=int(DonatorInfo.objects.last().total_amount if DonatorInfo.objects.last() else 5647) + amount)
        donator_temp.save()

        print('\nData:', request.POST)
        print(f'Total Donated: {DonatorInfo.objects.last().total_amount}')
        print(f'Donators: {DonatorInfo.objects.all()}')

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=int(amount * 7563),
            currency="inr",
            description=f"{request.POST['desciption']}\nAddress - {request.POST['address']}\nCountry - {request.POST['country']}"
        )

    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'donations/success.html', {'amount': amount})
