from rest_framework import serializers

from .models import Cart, CartContent
from menuapp.serializers import MenuSerializer


class CartContentSerializer(serializers.ModelSerializer):
    from menuapp.serializers import MenuOnlySerializer
    menu = MenuOnlySerializer()

    class Meta:
        model = CartContent
        fields = (
            'cart',
            'quantity',
            'menu'
        )


class CartContentOnlySerializer(serializers.ModelSerializer):
    from menuapp.serializers import MenuOnlySerializer
    menu = MenuOnlySerializer()

    class Meta:
        model = CartContent
        fields = (
            'quantity',
            'menu'
        )


class CartSerializer(serializers.ModelSerializer):
    cart_content = CartContentOnlySerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'user',
            'checkedOut',
            'status',
            'checkOutTime',
            'createdDate',
            'lastUpdated',
            'cart_content'
        )


class CartOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            'id',
            'user',
            'checkedOut',
            'status',
            'checkOutTime',
            'createdDate',
            'lastUpdated'
        )
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