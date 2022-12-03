from django.db import models
from django.utils import timezone
# Create your models here.
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
    createdDate = models.DateTimeField(null = True)
    lastUpdated = models.DateTimeField(null = True)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.createdDate = timezone.now()
        self.lastUpdated = timezone.now()
        return super(Cart, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.userId} - {self.checkedOut} - {self.status} - {self.checkOutTime} - {self.createdDate} - {self.lastUpdated}"