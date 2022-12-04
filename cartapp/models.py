from django.db import models
from django.contrib.auth.models import User

from menuapp.models import Menu


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checkedOut = models.BooleanField(default=False)
    status = models.CharField(max_length=30, choices=(
        ('menunggu_pembayaran', 'menunggu_pembayaran'),
        ('diproses', 'diproses'),
        ('siap_diambil', 'siap_diambil')
    ), default="menunggu_pembayaran")
    checkOutTime = models.DateTimeField(default=None, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.checkedOut} - {self.status} - {self.checkOutTime} - {self.createdDate} - {self.lastUpdated}"


class CartContent(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_content')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.cart.pk} - {self.menu.name} - {self.quantity}"
