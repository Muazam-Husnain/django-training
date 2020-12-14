import pytz
from datetime import datetime, timezone
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class SiteConfigration(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    values = models.JSONField(default={})

class Profile(models.Model):
    GENDER_CHOICES = [('M','Male'), ('F','Female')]
    TIMEZONE_CHOICES = zip(pytz.all_timezones, pytz.all_timezones)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nick_name = models.CharField(max_length=50, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    bio = models.TextField(max_length=500, null=True)
    timezone = models.CharField(max_length=32, default='UTC', choices=TIMEZONE_CHOICES)


class TripsUser(User):
    class Meta:
        proxy = True

    def is_staff_member(user):
        return user.groups.filter(name='staff').exists()

    def is_su_member(user):
        return user.groups.filter(name='superuser').exists()


class Host(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Trip(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateField()
    price = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL)
    host = models.ForeignKey('Host', on_delete=models.CASCADE, null=True)
    poster = models.ImageField(null=True)

    start_location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='start_location', null=True)
    destination_location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)
    trip_policy = models.TextField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.now()
        return super(Trip, self).save(*args, **kwargs)

    @property
    def total_days(self):
        return (datetime.strptime(str(self.end_date), "%Y-%m-%d") -
                datetime.strptime(str(self.start_date), "%Y-%m-%d")).days

    def __str__(self):
        return self.title

class TripSchedule(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    Over_ridden_price = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=1)

class Itenrary(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    day_number = models.CharField(max_length=3)
    places = models.TextField(null=True)
    description = models.TextField(null=True)
