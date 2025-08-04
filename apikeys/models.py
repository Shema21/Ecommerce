from django.db import models
from django.conf import settings
import uuid

class APIKey(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
