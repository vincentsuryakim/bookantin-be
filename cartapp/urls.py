from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('cart-content', CartContentViewSet, basename='cart-content')
router.register('cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]
