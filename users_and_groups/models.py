from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone_number = models.TextField(max_length=15, unique=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "profile"

