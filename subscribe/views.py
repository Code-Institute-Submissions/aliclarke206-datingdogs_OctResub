from django.shortcuts import render

from .forms import SubscriptionForm

# Create your views here.


def view_subscribe(request):
    """ A view that renders the subscribe page """
    subscription_form = SubscriptionForm()
    template = 'subscribe/subscribe.html'
    context = {
        'subscription_form': subscription_form,
    }

    return render(request, template, context)
