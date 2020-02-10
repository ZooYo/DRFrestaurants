from django.contrib import admin

# Register your models here.
from users_and_groups.models import Profile

admin.site.register(Profile)