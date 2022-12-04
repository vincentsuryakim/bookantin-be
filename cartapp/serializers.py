from rest_framework import serializers

from .models import Cart, CartContent
from menuapp.serializers import MenuSerializer

class CartContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartContent
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

class CartCheckoutTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['checkOutTime']

class CartContentHistorySerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    cart = CartCheckoutTimeSerializer()

    class Meta:
        model = CartContent
        fields = "__all__"