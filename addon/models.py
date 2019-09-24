from addon.fields import NonStrippingTextField
from core.models import UUIDPrimaryKeyMixin
from django.db import models
from markupfield.fields import MarkupField


class Platform(UUIDPrimaryKeyMixin, models.Model):
    identifier = models.SlugField(max_length=30)

    def __str__(self):
        return f"{self.identifier}"


class Addon(UUIDPrimaryKeyMixin, models.Model):
    namespace = models.ForeignKey("namespace.Namespace", related_name="addons")
    identifier = models.CharField(max_length=255)
    description = MarkupField(help_text="in markdown")

    def __str__(self):
        return f"{self.namespace}/{self.identifier}"


class AddonVersion(UUIDPrimaryKeyMixin, models.Model):
    addon = models.ForeignKey("Addon", related_name="addonversions")
    identifier = models.CharField(
        max_length=255, help_text="`1.0` or `master` or `1.2-beta`"
    )
    yaml = NonStrippingTextField()
    platforms = models.ManyToManyField(
        "Platform", help_text="Platforms this tag of the addon supports"
    )

    def __str__(self):
        return f"{self.addon}:{self.identifier}"
