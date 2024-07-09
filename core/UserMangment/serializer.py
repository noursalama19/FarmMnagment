from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    class Meta:
      model = User
      fields = ['id', 'username', 'phone','first_name','last_name','email','address','password' ]
      extra_kwargs = {'password': {'write_only': True}}
      
   
    def create(self, validated_data):
       
        password = validated_data.pop('password', None)
        
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
    def update(self, instance, validated_data):
        
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        new_password = validated_data.get('new_password',None)
        if new_password:
            instance.set_password(new_password)

        instance.save()
        return instance
        
        




