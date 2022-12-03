from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.forms.models import model_to_dict
from django.utils import timezone

from bookantinauth.permissions import IsCustomer

from .models import Cart, CartContent
from .serializers import CartContentSerializer, CartSerializer

class CartContentViewSet(viewsets.ModelViewSet):
    queryset = CartContent.objects.all()
    serializer_class = CartContentSerializer
    http_method_class = ['get', 'post', 'put', 'delete']
    permission_classes = (IsCustomer, )

    @action(detail=True, methods=['get'])
    def get_by_CartId(self, request, pk=None):
        queryset = CartContent.objects.filter(cartId=pk)
        serializer = CartContentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def get_by_MenuId_CartId(self, request):
        data = request.data
        menuId = data['menuId']
        cartId = data['cartId']

        cartContent = CartContent.objects.get(cart=cartId, menu=menuId)

        serializer = CartContentSerializer(cartContent)
        return Response(serializer.data)
        
    @action(detail=False, methods=['post'])
    def update_quantity_by_cartId_menuId(self, request):
        data = request.data
        cartId = data['cartId']
        menuId = data['menuId']
        newQuantity = data['quantity']

        cartContent = CartContent.objects.filter(cartId__exact=cartId).get(menuId__exact=menuId)
        cartContent.quantity = newQuantity
        cartContent.save()

        serializer = CartContentSerializer(data=model_to_dict(cartContent))
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)
        
    @action(detail=False, methods=['post'])
    def delete_by_CartId_MenuId(self, request):
        data = request.data
        cartId = data['cartId']
        menuId = data['menuId']

        cartContent = CartContent.objects.filter(cartId__exact=cartId).filter(menuId__exact=menuId)
        cartContent.delete()
        return Response("berhasil dihapus")

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    http_method_class = ['get', 'post', 'put', 'delete']
    permission_classes = (IsCustomer, )

    @action(detail=True, methods=['get'])
    def set_checkout_true_by_id(self, request, pk):
        cart = Cart.objects.get(id__exact=pk)
        cart.checkedOut = True
        cart.checkOutTime = timezone.now()
        cart.save()

        serializer = CartSerializer(data=model_to_dict(cart))
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(detail=False, methods=['post'])
    def update_status_by_id(self, request):
        data = request.data
        cartId = data['id']
        newStatus = data['status']

        cart = Cart.objects.get(id__exact=cartId)
        cart.status = newStatus
        cart.save()

        serializer = CartSerializer(data=model_to_dict(cart))
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)
        
    @action(detail=True,methods=['get'])
    def delete(self, request, pk):
        cart = Cart.objects.get(id__exact=pk)
        cart.delete()
        return Response("cart berhasil dihapus")
        