from django.contrib import admin

from .models import Cart, CartContent

# Register your models here.

admin.site.register(Cart)
admin.site.register(CartContent)