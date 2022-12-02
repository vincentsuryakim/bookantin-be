from rest_framework import viewsets
from .models import Cart,CartContent
from .serializers import CartContentSerializer,CartSerializer
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.decorators import action
from bookantinauth.permissions import IsSellerVerified,IsCustomer
from bookantinauth.models import Seller
from django.core import serializers
import json
class CartContentViewSet(viewsets.ModelViewSet):
    
    queryset = CartContent.objects.all()
    serializer_class = CartContentSerializer
    http_method_class = ['get', 'post', 'put', 'delete']

    def get_permissions(self):
        if self.action in ['create','get_by_CartId','get_by_Menuid_CartId','update_quantity_by_cartId_menuId']:
            self.permission_classes = (IsCustomer, )
        return super().get_permissions()
    
    @action(detail=True, methods=['get'])
    def get_by_CartId(self,request,pk=None):
        # try:
        cartContent = CartContent.objects.filter(cartId__exact=pk)
        response = CartContentSerializer(cartContent,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    @action(detail=False, methods=['post'])
    def get_by_MenuId_CartId(self,request):
        
        data = request.data
        menuId = data['menuId']
        cartId = data['cartId']
        cartContent = CartContent.objects.filter(cartId__exact=cartId).get(menuId__exact=menuId)
        serializer = CartContentSerializer(data=model_to_dict(cartContent))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    @action(detail=False, methods=['post'])
    def update_quantity_by_cartId_menuId(self,request):
        
        data = request.data
        cartId = data['cartId']
        menuId = data['menuId']
        newQuantity = data['quantity']
        cartContent = CartContent.objects.filter(cartId__exact=cartId).get(menuId__exact=menuId)
        cartContent.quantity = newQuantity
        cartContent.save()
        serializer = CartContentSerializer(data=model_to_dict(cartContent))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)