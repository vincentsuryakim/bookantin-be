from django.db import models
from rest_framework.authtoken.admin import User


# Create your models here.
class Cart(models.Model):
    checkedOut = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', default=False)
    # status = models.


class CartContent(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='contents')
    # menu = models.ForeignKey(Menu, on_delete=models.CASCADE(, related_name='menu'))
