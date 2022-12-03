from django.contrib import admin

from .models import BooKantinAPIToken, Seller, UserExtension
from tesapp.models import Cart,CartContent
# Register your models here.

admin.site.register(BooKantinAPIToken)
admin.site.register(Seller)
admin.site.register(UserExtension)
admin.site.register(Cart)
admin.site.register(CartContent)