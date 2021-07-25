from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_dogs, name='dogs'),
    path('<dog_id>', views.dog_detail, name='dog_detail'),
]