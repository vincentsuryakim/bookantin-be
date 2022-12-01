from rest_framework import viewsets

from .models import Menu
from .serializers import MenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(seller__verified = True)
    serializer_class = MenuSerializer
    http_method_class = ['get']
