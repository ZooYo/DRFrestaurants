from django.db import models
from django.contrib.auth.models import User
from basic_restaurants.models import Restaurant


class Reservation(models.Model):
    user_object = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_object = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    reservation_start_time = models.DateTimeField()
    reservation_end_time = models.DateTimeField()

    class Meta:
        db_table = "reservations"

