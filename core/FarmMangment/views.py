from rest_framework import viewsets,status,permissions
from rest_framework.permissions import IsAuthenticated
from .models import Farm, Crop, Animal
from .serializer import FarmSerializer, CropSerializer, AnimalSerializer
from rest_framework.response import Response
from UserMangment.jwt import getUser
from FarmMangment.api.authentication import JWTAuthentication
from UserMangment.models import User


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()  
    serializer_class = FarmSerializer
    
    def get_user_from_payload(self):
        authenticated, payload = getUser(self.request)
        return User.objects.get(pk=payload['id'])
   

    def get_queryset(self):
         user = self.get_user_from_payload()
         return Farm.objects.filter(owner=user)

    def create(self, request):
        user = self.get_user_from_payload()
        print(user.id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=user)  
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        farm = self.get_object()
        user = self.get_user_from_payload() 
        if farm.owner != user:
            return Response({'error': 'You are not authorized to update this farm.'}, status=status.HTTP_403_FORBIDDEN)
          
        serializer = self.get_serializer(farm, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
      
      
      
      
      

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()  
    serializer_class = CropSerializer
    
    def get_user_from_payload(self):
        authenticated, payload = getUser(self.request)
        return User.objects.get(pk=payload['id'])
   

    def get_queryset(self):
         user = self.get_user_from_payload()
         return Crop.objects.filter(farm__owner=user)

    def create(self, request):
        user = self.get_user_from_payload()
        print(user.id)
        serializer = self.get_serializer(data=request.data)
        farm=Farm.objects.get(id=request.data['farm'])
        if user==farm.owner:
          serializer.is_valid(raise_exception=True)
          serializer.save()  
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'You are not authorized to add crops in  this farm.'}, status=status.HTTP_403_FORBIDDEN)

      
    def update(self, request, pk=None):
        crop= self.get_object()
        user = self.get_user_from_payload() 
        if crop.farm.owner != user:
            return Response({'error': 'You are not authorized to update this farm.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(crop, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
      
      
      
class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()  
    serializer_class = AnimalSerializer
    
    def get_user_from_payload(self):
        authenticated, payload = getUser(self.request)
        return User.objects.get(pk=payload['id'])
   

    def get_queryset(self):
        user = self.get_user_from_payload()
        return Animal.objects.filter(farm__owner=user)

    def create(self, request):
        user = self.get_user_from_payload()
        print(user.id)
        serializer = self.get_serializer(data=request.data)
        farm=Farm.objects.get(id=request.data['farm'])
        if user==farm.owner:
          serializer.is_valid(raise_exception=True)
          serializer.save()  
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'You are not authorized to add animal in  this farm.'}, status=status.HTTP_403_FORBIDDEN)

       

    def update(self, request, pk=None):
        animal= self.get_object()
        user = self.get_user_from_payload()
        if animal.farm.owner != user:
            return Response({'error': 'You are not authorized to update the animal.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(animal, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
      
      
      
