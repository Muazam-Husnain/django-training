from rest_framework import serializers
from .models import Host, Location, Trip, Itenrary, Booking


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
        return response


class BookingSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

    class Meta:
        model = Booking
        fields = '__all__'
