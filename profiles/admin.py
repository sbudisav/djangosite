from django.contrib import admin

from .models import UserProfile, UserPlant, Friend

admin.site.register(UserProfile)
admin.site.register(UserPlant)
admin.site.register(Friend)