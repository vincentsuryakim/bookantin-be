from django.urls import path

from .views import *
urlpatterns = [
    path('add_cart', add_cart),
    path('add_cart_content', add_cart_content),
    path('get_cart_content', get_cart_content_by_Cartid),
    path('get_cart', get_cart_by_id),
    
]