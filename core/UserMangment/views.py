from django.shortcuts import render
from rest_framework import generics,mixins,status
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User
from django.core.exceptions import ValidationError
from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from datetime import datetime,timedelta
import jwt
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.exceptions import AuthenticationFailed
from FarmMangment.api.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .jwt import getUser
# Create your views here.
 
 
    

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                username = serializer.data['username']
                user = User.objects.filter(username=username).first()
                payload = {
                       'id': user.id,
                       'exp': datetime.utcnow() + timedelta(days=24), 
                       'iat': datetime.utcnow(),
                }

                token = jwt.encode(payload, 'secret', algorithm='HS256')
                response = Response(status=status.HTTP_201_CREATED)
                response.set_cookie(key='jwt', value=token, httponly=True)
                response.data = {
                    'jwt': token,
                    'data': serializer.data,
                }
                return response
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            raise AuthenticationFailed('User not found!')

        payload = {
            'id': user.id,
           'exp': datetime.utcnow() + timedelta(days=24), 
          'iat': datetime.utcnow(),
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token,
            'id': user.id,
            
        }
        return response
    
    
    
    

class InfoUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer  

    def get_queryset(self):
        return User.objects.all()

    def get_object(self):
        authenticated, payload = getUser(self.request)
        user_id = payload['id']

        try:
            person_instance = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            person_instance = None

        return person_instance

    def update(self, request, *args, **kwargs):
        person_instance = self.get_object()

        if person_instance is None:
            return Response({'error': 'Person not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(person_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)







