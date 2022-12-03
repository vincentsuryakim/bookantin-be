from rest_framework import viewsets
from .models import Menu
from .serializers import MenuOnlySerializer, MenuSerializer
from rest_framework.response import Response
from django.forms.models import model_to_dict

from bookantinauth.permissions import IsSellerVerified
from bookantinauth.models import Seller

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(seller__verified = True)
    serializer_class = MenuSerializer
    http_method_class = ['get', 'post', 'put', 'delete']

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'create']:
            self.permission_classes = (IsSellerVerified, )
        return super().get_permissions()

    def create(self, request):
        data = request.data
        user = request.user

        data['seller'] = user.seller.pk

        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    
    def update(self, request, pk=None):
        data = request.data
        user = request.user
 
        menu = Menu.objects.get(id=pk)

        if menu.seller.user.pk != user.pk:
            return Response('You are not authorized to update this menu.', status=403)
        
        if 'name' in data:
            menu.name = data['name']
        else:
            data['name'] = menu.name
        if 'price' in data:
            menu.price = data['price']
        else:
            data['price'] = menu.price
        if 'type' in data:
            menu.type = data['type']
        else:
            data['type'] = menu.type
        
        serializer = MenuOnlySerializer(menu, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        user = request.user

        menu = Menu.objects.get(id=pk)

        if menu.seller.user.pk != user.pk:
            return Response('You are not authorized to delete this menu.', status=403)

        menu.delete()
        return Response('Menu deleted successfully')
    