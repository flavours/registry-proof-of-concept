from addon.models import Addon, AddonVersion
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response


class AboutViewSet(viewsets.ViewSet):
    def list(self, request):

        return Response(
            {
                "version": settings.VERSION,
                "addons_count": Addon.objects.all().count(),
                "addonsversions_count": AddonVersion.objects.all().count(),
            }
        )
