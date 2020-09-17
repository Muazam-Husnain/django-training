from django.db import models

class Trip(models.Model):
    trip_title = models.CharField(max_length=60)
    trip_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
