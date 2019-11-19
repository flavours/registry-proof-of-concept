from addon.fields import NonStrippingTextField
from core.models import UUIDPrimaryKeyMixin
from django.contrib.postgres.fields import JSONField
from django.db import models
from markupfield.fields import MarkupField
from rest_framework.reverse import reverse


class Stack(UUIDPrimaryKeyMixin, models.Model):
    identifier = models.SlugField(max_length=30)

    def __str__(self):
        return f"{self.identifier}"

    def get_api_url(self, request=None):
        return reverse("stack-detail", args=[self.pk], request=request)


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
    config = JSONField(blank=True, default=dict)
    stacks = models.ManyToManyField(
        "Stack", help_text="Stacks this tag of the addon supports"
    )

    def __str__(self):
        return f"{self.addon}:{self.identifier}"
