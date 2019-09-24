from django.contrib import admin

from .models import Addon, AddonVersion, Platform


admin.site.register(Addon)
admin.site.register(AddonVersion)
admin.site.register(Platform)
