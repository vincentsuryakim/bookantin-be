from django.db import models
from django.conf import settings

import os
import binascii

# Create your models here.

class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="seller")
    description = models.TextField(default="", null=True, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {'Verified' if self.verified else 'Not Verified'}"

class UserExtension(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_extension")
    type = models.CharField(max_length=10, choices=(('SELLER', 'SELLER'), ('CUSTOMER', 'CUSTOMER')), default="CUSTOMER")

    def __str__(self):
        return f"{self.user.username} - {self.type}"

class BooKantinAPIToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return f"{self.user.username} - {self.key}"
