from django.conf import settings
from django.db import models
from django.utils import timezone

from menuapp.models import Menu


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart', default=False)
    checkedOut = models.BooleanField(default=False)
    status = models.CharField(max_length=30, choices=(
    ('menunggu_pembayaran', 'menunggu_pembayaran'), ('diproses', 'diproses'), ('siap_diambil', 'siap_diambil')),
                              default="menunggu_pembayaran")
    checkOutTime = models.DateTimeField(null=True)
    createdDate = models.DateTimeField(auto_now_add=True, null=True)
    lastUpdated = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.createdDate = timezone.now()
        self.lastUpdated = timezone.now()
        return super(Cart, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.checkedOut} - {self.status} - {self.checkOutTime} - {self.createdDate} - {self.lastUpdated}"


class CartContent(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='contents')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu')
    currentPrice = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.cart} - {self.menu} - {self.quantity}"
