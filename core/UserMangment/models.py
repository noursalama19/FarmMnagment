from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(AbstractUser):
    phone = PhoneNumberField(region="EG") 
    address = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    email=models.EmailField(max_length=255,unique=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']
    
    
