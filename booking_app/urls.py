from booking_project.urls import path
from booking_app import views as booking_app


urlpatterns = [
    path('', booking_app.index, name = 'index'),
    path('booking', booking_app.add_booking, name = 'booking'),
    path('home', booking_app.home, name = 'home')
]

