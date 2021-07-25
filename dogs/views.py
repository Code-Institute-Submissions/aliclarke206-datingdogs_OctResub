from django.shortcuts import render
from .models import Dog

# Create your views here.

def all_dogs(request):
    """ A view to show all dogs, including sorting and search queries """

    dogs = Dog.objects.all()

    context = {
        'dogs': dogs,
    }

    return render(request, 'dogs/dogs.html', context)