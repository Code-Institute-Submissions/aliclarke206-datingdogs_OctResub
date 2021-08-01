from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from .forms import SubscriptionForm
from .models import Subscription
from dogs.models import Dog
import stripe

# Create your views here.


def subscribe(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'country': request.POST['country'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
        }

        subscription_form = SubscriptionForm(form_data)
        if subscription_form.is_valid():
            subscription = subscription_form.save()
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('subscribe_success', args=[subscription.member_number]))

         else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:

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

def subscribe_success(request, member_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    subscribe = get_object_or_404(Subscription, member_number=member_number)
    messages.success(request, f'Subscription successfully processed! \
        Your order number is {member_number}. A confirmation \
        email will be sent to {subscribe.email}.')


    template = 'subscribe/subscribe_success.html'
    context = {
        'subscribe': subscribe,
    }

    return render(request, template, context)
