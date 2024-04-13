from .models import Property, Reservation
from rest_framework import serializers
from useraccount.serializers import UserSerializer

class PropertiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id',
            'title',
            'price_per_night',
            'image_url'
        ]

class PropertiesDetailSerializer(serializers.ModelSerializer):
    landlord = UserSerializer(read_only=True ,many=False)
    class Meta:
        model = Property
        fields = [
            'id',
            'title',
            'description',
            'bedrooms',
            'bathrooms',
            'guests',
            'price_per_night',
            'image_url',
            'landlord'
        ]

class ReservationsSerializer(serializers.ModelSerializer):
    property = PropertiesDetailSerializer(many=False, read_only=True)
    class Meta:
        model = Reservation
        fields = [
            'property', 'start_date', 'end_date', 'guests', 'number_of_nights', 'total_price'
        ]