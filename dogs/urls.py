from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_dogs, name='dogs'),
    path('<int:dog_id>/', views.dog_detail, name='dog_detail'),
    path('add/', views.add_dog, name='add_dog'),
    path('edit/<int:dog_id>/', views.edit_dog, name='edit_dog'),
    path('delete/<int:dog_id>/', views.delete_dog, name='delete_dog'),
]