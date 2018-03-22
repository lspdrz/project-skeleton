from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)

    class Meta:
        ordering = ('created',)
