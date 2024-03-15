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
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        # station = request.POST.get('station')
        clas = request.POST.get('class')
        date = request.POST.get('date')
        time = request.POST.get('time')
        place = Place.objects.get(id=1)
        station = Station.objects.get(id=1)
        
        booking = Booking(station=station, place=place, date=date, time=time)
        booking.save()
        
    return render (request, 'booking_app/booking.html')

def home(request):
    return render(request, 'booking_app/home.html')



