from django.db import models
from UserMangment.models import User

# Create your models here.
Type_Of_Crops=[("Fruits","Fruits"),("Vegetables","Vegetables"),("Legumes","Legumes"),("Grains","Grains")]


class Farm(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Crop(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255,choices=Type_Of_Crops )
    planting_date = models.DateField()
    harvest_date = models.DateField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

class Animal(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    birth_date = models.DateField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    