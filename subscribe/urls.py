from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('subscribe_success/<member_number>', views.subscribe_success, name='subscribe_success'),
    path('wh/', webhook, name='webhook'),
]
