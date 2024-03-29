from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 200)
    surname = models.CharField(max_length = 200)


class Place(models.Model):
    place = models.CharField(max_length = 3)

class Station(models.Model):
    name = models.CharField(max_length = 100)

class Booking(models.Model):
    place = models.ForeignKey(Place, on_delete = models.SET_NULL, null = True)
    date = models.DateField()
    time = models.TimeField(blank=True, null= True)
    station = models.ForeignKey(Station , on_delete = models.SET_NULL, null = True)



