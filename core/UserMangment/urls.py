from django.urls import path
from .views import RegisterView,Login,InfoUpdate

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    
    path("register/", RegisterView.as_view()),
 
    
    path("info-update/", InfoUpdate.as_view()),
    
    path("login", Login.as_view()),
    
   
    
    
    
    
]