from django.db import models

from bookantinauth.models import Seller

# Create your models here.
class Menu(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='menu')
    name = models.CharField(max_length=512)
    price = models.IntegerField()
    type = models.CharField(max_length=10, choices=(('FOOD', 'FOOD'), ('DRINK', 'DRINK')), default="FOOD")

    def __str__(self):
        return f"{self.name} - {self.seller.user.username} - {self.price} - {self.type}"