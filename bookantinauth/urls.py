from django.urls import path, include
from rest_framework import routers

from .views import user_login, user_logout, get_user_data, user_register, SellerViewSet

router = routers.DefaultRouter()
router.register('seller', SellerViewSet, basename='seller')

urlpatterns = [
    path('', include(router.urls)),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('register', user_register, name='register'),
    path('get_user_data', get_user_data, name='get_user_data'),
]