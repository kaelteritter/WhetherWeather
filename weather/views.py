from django.conf import settings
from django.shortcuts import render

from .forms import LocationForm

from .utils import get_weather


def index(request):
    location_form = LocationForm()

    location = request.GET.get('name')
    weather = {}

    if location:
        weather = get_weather(settings.OPEN_WEATHER_API_ID, location, units='metric', lang='ru')
        
        if 'message' in weather and weather['message'] == 'city not found':
            return render(request, '404.html', status=404, context={'location_form': location_form})

    return render(request, 'index.html', {'location_form': location_form, 'weather': weather})
    
