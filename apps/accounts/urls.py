from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegisterAPIView


app_name = 'accounts'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('register', UserRegisterAPIView.as_view(), name='register'),
]
