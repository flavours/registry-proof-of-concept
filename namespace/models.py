from core.models import UUIDPrimaryKeyMixin
from django.db import models


class Namespace(UUIDPrimaryKeyMixin, models.Model):
    identifier = models.SlugField(max_length=30)

    def __str__(self):
        return f"{self.identifier}"
