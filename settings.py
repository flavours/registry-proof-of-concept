# -*- coding: utf-8 -*-

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    "aldryn-addons",
    "aldryn-django",
    "aldryn-sso",
    # </INSTALLED_ADDONS>
]

MIDDLEWARE_CLASSES = []

import aldryn_addons.settings


aldryn_addons.settings.load(locals())


# all django settings can be altered here

INSTALLED_APPS.extend(  # noqa:F821
    ["rest_framework", "addon", "namespace", "corsheaders"]
)
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
        "rest_framework.renderers.StaticHTMLRenderer",
    ),
}

MIDDLEWARE_CLASSES.insert(0, "corsheaders.middleware.CorsMiddleware")

CORS_ORIGIN_ALLOW_ALL = True

VERSION = "0.1"
