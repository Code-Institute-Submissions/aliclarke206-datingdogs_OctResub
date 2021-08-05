from django.urls import path
from . import views

urlpatterns = [
    path('', views.direct_message, name='direct_message')
]