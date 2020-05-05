from django.contrib import admin

from .models import PublicProfile, PrivateProfile, UserPlant

admin.site.register(PublicProfile)
admin.site.register(PrivateProfile)
admin.site.register(UserPlant)