from django.contrib import admin

from .models import UserProfile, UserPlant, FollowedUser

admin.site.register(UserProfile)
admin.site.register(UserPlant)
admin.site.register(FollowedUser)