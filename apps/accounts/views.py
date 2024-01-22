from rest_framework.permissions import BasePermission
from .serializers import UserRegisterSerializer
from rest_framework.generics import CreateAPIView


class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer


__all__ = ['UserRegisterAPIView']