from rest_framework import serializers
from .models import Host, Location, Trip, Itenrary


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['host_name', 'host_number']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['location_name']


class TripSerializer(serializers.ModelSerializer):
    host = HostSerializer()
    start_location = LocationSerializer()
    destination_location = LocationSerializer()
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Trip
        fields = '__all__'

