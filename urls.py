# -*- coding: utf-8 -*-
import aldryn_addons.urls
from addon.views import AddonVersionViewSet, AddonViewSet, StackViewSet
from aldryn_django.utils import i18n_patterns
from core.views import AboutViewSet
from django.conf.urls import include, url
from namespace.views import NamespaceViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"addonversions", AddonVersionViewSet)
router.register(r"addons", AddonViewSet)
router.register(r"platforms", StackViewSet)  # legacy shim
router.register(r"stacks", StackViewSet)
router.register(r"namespaces", NamespaceViewSet)
router.register(r"about", AboutViewSet, basename="about")


urlpatterns = (
    [
        url(r"^", include(router.urls)),
        # url('about/', AboutViewSet.as_view()),
        url(r"^api-auth/", include("rest_framework.urls")),
    ]
    + aldryn_addons.urls.patterns()
    + i18n_patterns(
        *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
    )
)
