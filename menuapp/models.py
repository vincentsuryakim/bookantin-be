from django.db import models

# Create your models here.
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey('bookantinauth.Seller', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=10, choices=(('FOOD', 'FOOD'), ('DRINK', 'DRINK')), default="FOOD")
