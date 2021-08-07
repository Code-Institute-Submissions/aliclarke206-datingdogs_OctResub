from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Subscription


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, subscription):
        """Send the user a confirmation email"""
        cust_email = subscription.email
        subject = render_to_string(
            'subscribe/confirmation_emails/confirmation_email_subject.txt',
            {'subscription': subscription})
        body = render_to_string(
            'subscribe/confirmation_emails/confirmation_email_body.txt',
            {'subscription': subscription, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )        


    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):

        """ Handle the payment_intent.succeeded webhook from Stripe"""
        intent = event.data.object
        self._send_confirmation_email(subscription)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe"""

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
