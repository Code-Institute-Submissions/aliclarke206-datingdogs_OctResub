from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_dogs, name='dogs'),
    path('<int:dog_id>/', views.dog_detail, name='dog_detail'),
    path('add/', views.add_dog, name='add_dog'),
]