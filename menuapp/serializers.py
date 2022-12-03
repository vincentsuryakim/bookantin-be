from rest_framework import serializers

from .models import Menu
from bookantinauth.serializers import SellerMenuSerializer

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'price', 'seller', 'type')
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['seller'] = SellerMenuSerializer(instance.seller).data

        return representation

class MenuOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'price', 'type')