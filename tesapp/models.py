from django.db import models

class CartContent(models.Model):
    cartId = models.IntegerField()
    menuId = models.IntegerField()
    quantity = models.IntegerField()
    def __str__(self):
        return f"{self.cartId} - {self.menuId} - {self.quantity}"

class Cart(models.Model):
    userId = models.IntegerField()
    checkedOut = models.BooleanField(default=False)
    status = models.CharField(max_length=30,choices=(('diproses','diproses'),('siap_diambil','siap_diambil')),default="diproses")
    checkOutTime = models.DateTimeField(null = True)
    createdDate = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.userId} - {self.checkedOut} - {self.status} - {self.checkOutTime} - {self.createdDate} - {self.lastUpdated}"