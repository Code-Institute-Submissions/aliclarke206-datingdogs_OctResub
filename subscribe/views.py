from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from .forms import SubscriptionForm
import stripe

# Create your views here.


def subscribe(request):
    """ A view that renders the subscribe page """
    subscription_form = SubscriptionForm()
    template = 'subscribe/subscribe.html'
    context = {
        'subscription_form': subscription_form,
        'stripe_public_key': 'pk_test_51JJKYXLhOLwgGIo6FooM9njTNm2yq3fSk27ubLKTXnkC1Pryh7w7Zr0FXYE86HsDaF2v37HZ8MMcbzLW46jcyz9K00cjiI9Ci4',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
