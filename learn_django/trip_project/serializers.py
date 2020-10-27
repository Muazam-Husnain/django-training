from rest_framework import serializers
from .models import Host, Location, Trip, Itenrary


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['name', 'number']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name']


class TripSerializer(serializers.ModelSerializer):
    host = HostSerializer(many=False, read_only=True)
    start_location = LocationSerializer(many=False, read_only=True)
    destination_location = LocationSerializer(many=False, read_only=True)
    created_by = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Trip
        fields = ['title', 'description', 'start_date', 'end_date', 'price', 'created_at',
                  'created_by', 'host', 'poster', 'destination_location', 'start_location',
                  'trip_policy', 'total_days']

