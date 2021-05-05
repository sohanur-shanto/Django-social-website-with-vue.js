from django.db import models
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize


class Oink(models.Model):
    body = models.CharField(max_length=300)

    created_by = models.ForeignKey(User, related_name='oinks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

