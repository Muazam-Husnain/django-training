from django.conf import settings
from django.db import models

class Trip(models.Model):
    trip_title = models.CharField(max_length=60)
    trip_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True, on_delete=models.SET_NULL)
    host_name = models.CharField(max_length=100, null=True)
    host_number = models.CharField(max_length=20, null=True)
    poster = models.ImageField(null=True)
    start_location = models.CharField(max_length=100, null=True)
    destination_location = models.CharField(max_length=100, null=True)
    destination_date = models.DateField(null=True)
    trip_policy = models.TextField(null=True)
    total_days = models.IntegerField(null=True)

class Itenrary(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    Day_number = models.CharField(max_length=3)
    date = models.DateField(null=True)
    places = models.TextField(null=True)
    description = models.TextField(null=True)
