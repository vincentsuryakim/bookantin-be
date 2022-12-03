from django.db import models
from django.conf import settings


# Create your models here.
class Cart(models.Model):
    class CartStatus(models.IntegerChoices):
        AWAITING_PAYMENT = 1
        PROCESSED = 2
        READY_FOR_PICKUP = 3

    checkedOut = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart', default=False)
    status = models.IntegerField(choices=CartStatus.choices, default=1)


class CartContent(models.Model):
    # Many to Many between cart and menu
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='contents')
    # menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu'))
