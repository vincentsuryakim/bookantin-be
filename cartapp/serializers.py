from rest_framework import serializers

from .models import Cart, CartContent


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
            'user',
            'checkedOut',
            'status',
            'checkOutTime',
            'createdDate',
            'lastUpdated',
            'cart_content'
        )
