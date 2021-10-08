from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('subscribe_success/<member_number>', views.subscribe_success,
         name='subscribe_success'),
    path('cache_subscribe_data/', views.cache_subscribe_data,
         name='cache_subscribe_data'),
    path('wh/', webhook, name='webhook'),
]
