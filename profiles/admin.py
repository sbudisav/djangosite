from django.contrib import admin

from .models import PublicProfile, PrivateProfile

admin.site.register(PublicProfile)
admin.site.register(PrivateProfile)