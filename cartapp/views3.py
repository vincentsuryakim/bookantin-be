from django.shortcuts import render
from .models import CartContent,Cart
from .forms import CartContentForm,CartForm
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict
# Create your views here.

SUCCESS_RESPONSE = JsonResponse({
            'pesan' : 'Success'
        })
# class FailedResponse:
#     def __init__(self,error):
#         self.error = error
#     def get_message():
#         return JsonResponse({
#             'pesan' : 'Failed'
#             'error' : self.error 
#         })
FAILED_RESPONSE = JsonResponse({
            'pesan' : 'Failed'
        })
@csrf_exempt
def add_cart_content(request):
    #try:
        body_unicode =request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cartContent = CartContent(cartId = body['cartId'],menuId=body['menuId'],quantity=body['quantity'])
        cartContent.save()
        
        return JsonResponse({"cartId":cartContent.cartId,"menuId":cartContent.menuId,"quantity":cartContent.quantity})
    #except:
        return FAILED_RESPONSE
@csrf_exempt
def add_cart(request):
    try:
        body_unicode =request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cart = Cart(userId=body['userId'])
        cart.save()
        return JsonResponse({"userId":cart.userId,"checkedOut":cart.checkedOut,"status":cart.status})
    except:
        return FAILED_RESPONSE
@csrf_exempt
def get_cart_by_id(request):
    try:
        body_unicode =request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cartId = body['id']
        cart = Cart.objects.get(id__exact=cartId)
        response = serializers.serialize('json',cart)
        return JsonResponse(response)
    except:
        return FAILED_RESPONSE
@csrf_exempt
def get_cart_content_by_Cartid(request):
    try:
        body_unicode =request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cartId = body['id']
        cartContent = CartContent.objects.all.filter(cartId__exact=cartId)
        response = serializers.serialize('json',cartContent)
        return JsonResponse(response)
    except:
        return FAILED_RESPONSE
def get_cart_content_by_Menuid_CartId(request):
    try:
        body_unicode =request.body.decode('utf-8')
        body = json.loads(body_unicode)
        menuId = body['menuId']
        cartId = body['cartId']
        cartContent = CartContent.objects.all.filter(menuId__exact=menuId).filter(cartId__exact=cartId)
        response = serializers.serialize('json',cartContent)
        return JsonResponse(response)
    except:
        return FAILED_RESPONSE

def set_checkout_true_by_id(request):
    try:
        body_unicode =request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cartId = body['id']
        cart = Cart.objects.get(id_exact=cartId)
        cart.checkout = True
        cart.save()
        response = serializers.serialize('json',cart)
        return JsonResponse(response)
    except:
        return FAILED_RESPONSE

def update_cart_status_by_id(request):
    try:
        body_unicode =request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cartId = body['id']
        newStatus = body['status']
        cart = Cart.objects.get(id_exact=cartId)
        cart.status = newStatus
        cart.save()
        response = serializers.serialize('json',cart)
        return JsonResponse(response)
    except:
        return FAILED_RESPONSE
def update_cart_content_quantity_by_cartId_menuId(request):
    try:
        body_unicode =request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cartId = body['cartId']
        menuId = body['menuId']
        newQuantity = body['quantity']
        cartContent = CartContent.objects.all.filter(cartId__exact=cartId).get(menuId__exact=menuId)
        cartContent.quantity = quantity
        cartContent.save()
        response = serializers.serialize('json',cartContent)
        return JsonResponse(response)
    except:
        return FAILED_RESPONSE
def delete_cart_content_by_CartId(request):
    try:
        body_unicode =request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cartId = body['id']
        cartContent = CartContent.objects.all.filter(id__exact=cartId)
        cartContent.delete()
        return SUCCESS_RESPONSE
    except:
        return FAILED_RESPONSE

def delete_cart_content_by_CartId_MenuId(request):
    try:
        body_unicode =request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cartId = body['cartId']
        menuId = body['menuId']
        cartContent = CartContent.objects.all.filter(cartId__exact=cartId).filter(menuId__exact=menuId)
        cartContent.delete()
        return SUCCESS_RESPONSE
    except:
        return FAILED_RESPONSE
def delete_cart_by_id(request):
    try:
        body_unicode =request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cartId = body['id']
        cart = Cart.objects.get(id_exact=cartId)
        cart.delete()
        return SUCCESS_RESPONSE
    except:
        return FAILED_RESPONSE

    