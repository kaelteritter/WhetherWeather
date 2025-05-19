from django.shortcuts import render

from .forms import LocationForm


def index(request):
    context = {
        'search_location_input': LocationForm()
    }
    return render(request, 'index.html', context=context)