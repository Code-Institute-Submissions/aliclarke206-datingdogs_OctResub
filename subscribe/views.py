from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from .forms import SubscriptionForm
import stripe

# Create your views here.


def subscribe(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY


    fee = round(35 * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=fee,
        currency=settings.STRIPE_CURRENCY,
    )
    """ A view that renders the subscribe page """
    subscription_form = SubscriptionForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')


    template = 'subscribe/subscribe.html'
    context = {
        'subscription_form': subscription_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
