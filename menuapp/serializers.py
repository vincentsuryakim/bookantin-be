from rest_framework import serializers

from .models import Menu
from bookantinauth.serializers import SellerMenuSerializer

class MenuSerializer(serializers.ModelSerializer):
    seller = SellerMenuSerializer()

    class Meta:
        model = Menu
        fields = ('id', 'name', 'price', 'seller', 'type')

class MenuOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'price', 'type')