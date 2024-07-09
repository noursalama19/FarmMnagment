from django.urls import path
from .views import RegisterView,Login,InfoUpdate,UserGetprofile,RefreshToken




urlpatterns = [
    
    path("register/", RegisterView.as_view()),
 
    
    path("info-update/", InfoUpdate.as_view()),
    
    path("login/", Login.as_view()),
    path("profile/", UserGetprofile.as_view()),
    path('refresh-token/', RefreshToken.as_view(), name='refresh-token'),
    
    
   
    
    
    
    
]
