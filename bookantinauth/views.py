from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError

from .models import Seller, UserExtension
from .serializers import LoginSerializer, RegisterSerializer, SellerSerializer
from .utils import generate_token

from bookantinauth.permissions import IsAdmin

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.filter(verified = True)
    serializer_class = SellerSerializer
    http_method_class = ['get']

class SellerAllViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    http_method_class = ['get', 'post', 'delete']
    permission_classes = [IsAdmin]

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            self.permission_classes = [IsAdmin]
        return super().get_permissions()

    def create(self, request):
        data = request.data
        try:
            seller = Seller.objects.get(id=data['id'])
            seller.verified = True
            seller.save()
            return Response('Seller verified successfully', status=201)
        except:
            return Response('Seller does not exist', status=404)

    def destroy(self, request, pk=None):
        user = request.user
        userId = Seller.objects.get(id=pk).user.pk
        User.objects.get(id = userId).delete()
        return Response('Seller deleted successfully', status=201)
        
@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def user_login(request):
    data = {}
    serializer = LoginSerializer(data=request.data)

    serializer.validate_attribute(request.data)
    user = authenticate(request=request,
                        username=request.data['username'], 
                        password=request.data['password'])
    if not user:
        data['response'] = 'Invalid username or password.'
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)   

    data['response'] = 'Sign-in successful.'
    data['token'] = generate_token(user)

    return Response(data=data, status=status.HTTP_200_OK)

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def user_register(request):
    data = {}
    serializer = RegisterSerializer(data=request.data)

    serializer.validate_attribute(request.data)
    
    try:
        user = User.objects.create_user(username=request.data['username'],
                                        password=request.data['password'],
                                        email=request.data['email'],
                                        first_name=request.data['first_name'],
                                        last_name=request.data['last_name'])
    except IntegrityError as e:
        data['response'] = 'Username or email already exists.'
        return Response(data=data, status=status.HTTP_409_CONFLICT)
    except:
        data['response'] = 'Something went wrong.'
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    

    user_extension = UserExtension.objects.create(user=user, type=request.data['type'])

    if request.data['type'] == 'SELLER':
        seller = Seller.objects.create(user=user)
        seller.save()
    
    user.save()
    user_extension.save()

    data['response'] = 'User created successfully.'
    return Response(data=data, status=status.HTTP_201_CREATED)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def user_logout(request):
    request.auth.delete()
    logout(request)

    return Response('User logged out successfully')

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    user = request.user
    data = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'type': user.user_extension.type,
    }
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user_data(request):
    user = request.user
    data = request.data

    try:
        user.username = data['username']
        user.email = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.save()
        return Response('User data updated successfully', status=status.HTTP_200_OK)
    except IntegrityError as e:
        data['response'] = 'Username or email already exists.'
        return Response(data=data, status=status.HTTP_409_CONFLICT)
    except:
        data['response'] = 'Something went wrong.'
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)