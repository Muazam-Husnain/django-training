from datetime import datetime
from django.conf import settings
from django.db import models


class Host(models.Model):
    host_name = models.CharField(max_length=100)
    host_number = models.CharField(max_length=20)


class Location(models.Model):
    location_name = models.CharField(max_length=100)

class Trip(models.Model):
    trip_title = models.CharField(max_length=60)
    trip_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL)
    host = models.ForeignKey('Host', on_delete=models.CASCADE, null=True)
    poster = models.ImageField(null=True)

    start_location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='start_location', null=True)
    destination_location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)
    trip_policy = models.TextField(null=True)

    @property
    def total_days(self):
        return (datetime.strptime(str(self.end_date), "%Y-%m-%d") -
                datetime.strptime(str(self.start_date), "%Y-%m-%d")).days


class Itenrary(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    day_number = models.CharField(max_length=3)
    places = models.TextField(null=True)
    description = models.TextField(null=True)
