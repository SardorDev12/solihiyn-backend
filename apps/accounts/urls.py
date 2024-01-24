from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegisterAPIView, HomeAPIView,UserLogoutAPIView


app_name = 'accounts'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('logout/', UserLogoutAPIView.as_view(), name='user_logout'),
    path('home/', HomeAPIView.as_view(), name='home'),
]