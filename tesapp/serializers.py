from rest_framework import serializers

from .models import Cart,CartContent

#from bookantinauth.serializers import SellerMenuSerializer


class CartContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartContent
        fields = ('id', 'cartId', 'menuId', 'quantity')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'userId', 'checkedOut', 'status','checkOutTime','createdDate','lastUpdated')