from django.contrib import admin

from .models import BooKantinAPIToken, Seller, UserExtension

# Register your models here.

admin.site.register(BooKantinAPIToken)
admin.site.register(Seller)
admin.site.register(UserExtension)