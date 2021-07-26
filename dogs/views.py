from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Dog, Breed

# Create your views here.

def all_dogs(request):
    """ A view to show all dogs, including sorting and search queries """

    dogs = Dog.objects.all()
    query = None
    breeds = None

    if request.GET:
        if 'breed' in request.GET:
            breeds = request.GET['breed'].split(',')
            dogs = dogs.filter(breed__name__in=breeds)
            breeds = Breed.objects.filter(name__in=breeds)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('dogs'))
            
            queries = Q(location__icontains=query) | Q(description__icontains=query)
            dogs = dogs.filter(queries)

    context = {
        'dogs': dogs,
        'search_term': query,
        'current_breeds': breeds,
    }

    return render(request, 'dogs/dogs.html', context)


def dog_detail(request, dog_id):
    """ A view to show individual dog details """

    dog = get_object_or_404(Dog, pk=dog_id)

    context = {
        'dog': dog,
    }

    return render(request, 'dogs/dog_detail.html', context)