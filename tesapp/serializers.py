from rest_framework import serializers

from .models import Cart, CartContent

class CartContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartContent
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"