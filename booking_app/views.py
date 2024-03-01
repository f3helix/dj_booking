from django.shortcuts import render
from booking_app.models import *



def index(request):
    places = Place.objects.all()
    content = {'place':places, 'stations': Station.objects.all()}
    return render(request, 'booking_app/index.html', content)

def place_detale(request, place_id):
    place = Place.objects.get(id=place_id)
    content = {'place':place}
    
def add_booking(request):
    return render (request, 'booking_app/booking.html')





