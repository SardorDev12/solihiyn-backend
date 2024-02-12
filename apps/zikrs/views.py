from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.generics import RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q

from .models import Zikr
from .serializers import ZikrSerializer


class ZikrListCreateAPIView(ListCreateAPIView):
    serializer_class = ZikrSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_zikrs = Zikr.objects.filter(created_by=self.request.user)
        default_zikrs = Zikr.objects.filter(is_default=True)
        queryset = user_zikrs | default_zikrs
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class ZikrUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Zikr.objects.all()
    serializer_class = ZikrSerializer


class ZikrDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Zikr.objects.all()
    serializer_class = ZikrSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.is_default:
            return Response({"message": "Default items cannot be deleted."}, status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



class IncrementZikrCountView(UpdateAPIView):
    queryset = Zikr.objects.all()
    serializer_class = ZikrSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.count_val >= instance.count:
            instance.count_val = 1
            instance.save()
        else:
            instance.count_val += 1

        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
