from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError

from .serializers import LoginSerializer, RegisterSerializer
from .utils import generate_token

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
    
    user.save()
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
    }
    return Response(data=data, status=status.HTTP_200_OK)