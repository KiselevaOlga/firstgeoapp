from django.shortcuts import render, get_object_or_404
from mapapp.models import Measurement 
from mapapp.forms import MeasurementForm
from geopy.geocoders import Nominatim
from mapapp.utils import get_location_data
# Create your views here.
def calculate_distance(request):
    # since we already created our first object, we call with id 1
    object = get_object_or_404(Measurement, id=1)
    form = MeasurementForm(request.POST or None)
    geolocator = Nominatim(user_agent='mapapp')

    ip = '72.14.207.99'
    country, city, latit, longit = get_location_data(ip)
    print('location country', country)
    print('location city', city)
    print('location latit', latit)
    print('location longit', longit)
    location = geolocator.geocode(city)
    print("snjdn", location)
    if form.is_valid():
        # if commit form False than it tells django to not save it yet
        instance = form.save(commit=False)
        destination_ = form.cleaned_data['destination']
        destination = geolocator.geocode(destination_)
        dest_address = destination.address
        dest_latitude = destination.latitude
        dest_lonitude = destination.longitude
        dest_raw_data = destination.raw

        instance.location = 'New York'
        instance.distance = 3000.00
        #instance.save()

    context = {
        'distance': object,
        'form': form,
    }
    #or i can create templates folder in mapapp
    return render(request, 'index.html', context)