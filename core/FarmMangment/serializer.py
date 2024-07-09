from rest_framework import serializers
from .models import Farm, Crop, Animal

class FarmSerializer(serializers.ModelSerializer):
      
    owner = serializers.CharField(read_only=True)
    
    class Meta:
        model = Farm
        fields = ['id', 'name', 'location', 'size', 'owner']
        def validate(self, attrs):
    
          if 'owner' in attrs:
            raise serializers.ValidationError("Owner field cannot be updated.")
          return attrs
        
        def update(self, instance, validated_data):
          instance.name = validated_data.get('name', instance.name)
          instance.location = validated_data.get('location', instance.location)
          instance.size = validated_data.get('size', instance.size)
          instance.save()
          return instance
      
      

class CropSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Crop
        fields = ['id', 'name', 'type', 'planting_date', 'harvest_date', 'farm']
        
        def update(self, instance, validated_data):
          instance.name = validated_data.get('name', instance.name)
          instance.type = validated_data.get('type', instance.type)
          instance.planting_date = validated_data.get('planting_date', instance.planting_date)
          instance.harvest_date = validated_data.get('harvest_date', instance.harvest_date)
          
          instance.save()
          return instance
        

class AnimalSerializer(serializers.ModelSerializer):
 
    
    class Meta:
        model = Animal
        fields = ['id', 'name', 'species', 'birth_date', 'farm']
        
        def update(self, instance, validated_data):
          instance.name = validated_data.get('name', instance.name)
          instance.species = validated_data.get('type', instance.species)
          instance.birth_date = validated_data.get('birth_date', instance.birth_date)
          
          
          instance.save()
          return instance
