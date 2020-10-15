from rest_framework import serializers
from .models import Host, Location, Trip, Itenrary

class TripSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    start_location = serializers.StringRelatedField()
    destination_location = serializers.StringRelatedField()

    class Meta:
        model = Trip
        fields = '__all__'
