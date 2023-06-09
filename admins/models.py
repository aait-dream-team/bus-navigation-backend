import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

USER_TYPES = [("sys-admin", "System Administrator"), ("admin", "Administrator")]


class Admin(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(choices=USER_TYPES, max_length=150, default=USER_TYPES[0])
    class Meta:
        swappable = 'AUTH_USER_MODEL'
    def save(self, *args, **kwargs):
        self.email = self.username
        return super().save(*args, **kwargs)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)