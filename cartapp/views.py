import datetime

from django.forms.models import model_to_dict
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from bookantinauth.models import Seller
from bookantinauth.permissions import IsSellerVerified, IsCustomer
from .models import Cart, CartContent
from .serializers import CartContentSerializer, CartSerializer, CartContentHistorySerializer


class CartContentViewSet(viewsets.ModelViewSet):
    queryset = CartContent.objects.all()
    serializer_class = CartContentSerializer
    http_method_class = ['get', 'post', 'put', 'delete']
    permission_classes = (IsCustomer,)

    @action(detail=True, methods=['get'])
    def get_by_CartId(self, request, pk=None):
        user = request.user
        cart = Cart.objects.get(id=pk)
        queryset = cart.cart_content 
        if cart.user.pk != user.pk: 
            return Response('You are not authorized to access this cart.', status=403)

        serializer = CartContentOnlySerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def get_by_MenuId_CartId(self, request):
        data = request.data
        user = request.user
        menuId = data['menuId']
        cartId = data['cartId']
        cartContent = CartContent.objects.get(cart=cartId, menu=menuId)
        if cartContent.cart.user.pk != user.pk:
            return Response('You are not authorized to access this cart.', status=403)

        serializer = CartContentOnlySerializer(cartContent)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def add_quantity_by_cartId_menuId(self, request):
        data = request.data
        user = request.user
        cartId = data['cartId']
        menuId = data['menuId']
        newQuantity = data['quantity']

        cartContent = CartContent.objects.get(cart=cartId, menu=menuId)
        if cartContent.cart.user.pk != user.pk:
            return Response('You are not authorized to access this cart.', status=403)

        cartContent.quantity = cartContent.quantity + newQuantity
        cartContent.save()

        serializer = CartContentOnlySerializer(data=model_to_dict(cartContent))
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(detail=True, methods=['post'])
    def update_quantity(self, request, pk):
        data = request.data
        user = request.user
        cartContent = CartContent.objects.get(id=pk)
        if cartContent.cart.user.pk != user.pk:
            return Response('You are not authorized to update this cart.', status=403)
        cartContent.quantity = data['quantity']
        cartContent.save()
        serializer = CartContentOnlySerializer(data=model_to_dict(cartContent))
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(detail=False, methods=['post'])
    def delete_by_CartId_MenuId(self, request):
        data = request.data
        user = request.user
        cartId = data['cartId']
        menuId = data['menuId']

        cartContent = CartContent.objects.get(cart=cartId, menu=menuId)
        if cartContent.cart.user.pk != user.pk:
            return Response('You are not authorized to delete this cart.', status=403)
        cartContent.delete()
        return Response("berhasil dihapus")


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    http_method_class = ['get', 'post', 'put', 'delete']

    # permission_classes = (IsCustomer, IsSellerVerified)

    @action(detail=False, methods=['get'])
    @permission_classes([IsCustomer])
    def add(self, request):
        user = request.user
        cart = Cart(user=user)
        cart.save()
        serializer = CartOnlySerializer(data=model_to_dict(cart))
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(detail=True, methods=['get'])
    @permission_classes([IsCustomer])
    def set_checkout_true_by_id(self, request, pk):
        cart = Cart.objects.get(id=pk)
        user = request.user
        if cart.user.pk != user.pk:
            return Response('You are not authorized to update this cart.', status=403)

        cart.checkedOut = True
        cart.checkOutTime = timezone.now()
        cart.save()

        serializer = CartOnlySerializer(data=model_to_dict(cart))
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(detail=False, methods=['post'])
    @permission_classes([IsCustomer])
    def update_status_by_id(self, request):
        data = request.data
        user = request.user
        cartId = data['id']
        newStatus = data['status']

        cart = Cart.objects.get(id=cartId)
        if cart.user.pk != user.pk:
            return Response('You are not authorized to update this cart.', status=403)

        cart.status = newStatus
        cart.save()
        serializer = CartOnlySerializer(data=model_to_dict(cart))
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def accept_payment(self, request, pk=None):
        user = request.user
        cart = Cart.objects.get(id__exact=pk)
        if cart.status == "menunggu_pembayaran" and not cart.checkedOut:
            cart.checkedOut = True
            cart.status = "diproses"
            cart.checkOutTime = datetime.datetime.now()
            cart.save()

            return Response("Pembayaran diterima", status=200)

        else:
            return Response("Pembayaran gagal", status=402)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def get_processed_menu(self, request):

        user = request.user
        cart = list(Cart.objects.filter(status='diproses'))
        menu = []
        for c in cart:
            for m in c.cart_content.all():
                if m.menu.seller.user == user:
                    menu.append(m)
        serializer = CartContentOnlySerializer(menu, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    @permission_classes([IsCustomer])
    def delete(self, request, pk):
        user = request.user
        cart = Cart.objects.get(id__exact=pk)
        if cart.user.pk != user.pk:
            return Response('You are not authorized to delete this cart.', status=403)
        cart.delete()
        return Response("cart berhasil dihapus")


class GetSellerHistory(APIView):
    permission_classes = (IsSellerVerified,)

    def get(self, request):
        user = request.user

        seller = Seller.objects.get(user=user)
        cart_content = CartContent.objects.filter(menu__seller=seller).order_by('-cart__checkOutTime')

        serializer = CartContentHistorySerializer(cart_content, many=True)

        return Response(serializer.data)
