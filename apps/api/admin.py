from django.contrib.auth.models import Permission
from django.contrib import admin

from apps.api.models import Moderator

admin.site.register(Permission)
admin.site.register(Moderator)
