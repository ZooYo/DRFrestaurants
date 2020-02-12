from rest_framework import serializers
from reservations.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(read_only=True, source="restaurant.name")

    class Meta:
        model = Reservation
        fields = "__all__"


class ReservationUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ["reservation_start_time", "reservation_end_time"]
