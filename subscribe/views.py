from django.shortcuts import render

# Create your views here.


def view_subscribe(request):
    """ A view that renders the subscribe page """

    return render(request, 'subscribe/subscribe.html')
