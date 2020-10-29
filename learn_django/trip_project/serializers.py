from rest_framework import serializers
from .models import Host, Location, Trip, Itenrary


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        exclude = ['id']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ['id']


class TripSerializer(serializers.ModelSerializer):
    host = HostSerializer(many=False, read_only=True)
    start_location = LocationSerializer(many=False, read_only=True)
    destination_location = LocationSerializer(many=False, read_only=True)
    created_by = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Trip
        exclude = ['id']

