from django.contrib import admin

from .models import UserProfile, UserPlant

admin.site.register(UserProfile)
admin.site.register(UserPlant)