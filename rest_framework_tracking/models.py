from django.db import models
from .base_models import BaseAPIRequestLog


class APIRequestLog(BaseAPIRequestLog):
    verb = models.CharField(max_length=500, null=True, blank=True)
