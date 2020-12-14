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
    created_by = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Trip
        exclude = ['id', 'created_at']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['host'] = HostSerializer(instance.host).data
        response['start_location'] = LocationSerializer(instance.start_location).data
        response['destination_location'] = LocationSerializer(instance.destination_location).data
        # response['created_by'] = serializers.StringRelatedField()
        return response

