from django.shortcuts import render
from django.http import HttpResponse
from home.models import *
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.
def main(request,pay_id):
    p = Client.objects.get(pk=pay_id)
    context = {
        'client':p,
        'key':settings.STRIPE_PUBLISHABLE_KEY 
    }
    
    return render(request,'checkout.html',context)

def charge(request,charge_id):
    m = Client.objects.get(pk=charge_id)
    # m.status="Paid"
    # m.save()
    context = {
        'client':m,
    }
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='INR',
            description='A Django charge',
            source=request.POST['stripeToken'],
            
        )
    return render(request,'charge.html',context)