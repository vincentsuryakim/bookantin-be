from rest_framework import viewsets
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.response import Response

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(seller__verified = True)
    serializer_class = MenuSerializer
    http_method_class = ['get', 'post', 'put', 'delete']

    def list(self, request):
        queryset = Menu.objects.filter(seller__verified = True)
        serializer = MenuSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        seller = getDataFromToken(request)
        data['seller'] = seller.id
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def update(self, request, pk=None):
        data = request.data
        seller = getDataFromToken(request)
        data['seller'] = seller.id
        menu = Menu.objects.get(id=pk)
        serializer = MenuSerializer(menu, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        menu = Menu.objects.get(id=pk)
        menu.delete()
        return Response('Menu deleted successfully')
    
    def retrieve(self, request, pk=None):
        menu = Menu.objects.get(id=pk)
        serializer = MenuSerializer(menu, many=False)
        return Response(serializer.data)