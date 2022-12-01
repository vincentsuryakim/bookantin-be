from django.db import models

# Create your models here.
class CartContent(models.Model):
    cartId = models.IntegerField()
    menuId = models.IntegerField()
    quantity = models.IntegerField()

class Cart(models.Model):
    userId = models.IntegerField()
    checkedOut = models.BooleanField(default=False)
    status = models.CharField(max_length=30,default="diproses")