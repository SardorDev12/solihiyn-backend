from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.generics import RetrieveUpdateAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import F

from .models import Zikr
from .serializers import ZikrSerializer


class ZikrListCreateAPIView(ListCreateAPIView):
    serializer_class = ZikrSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Zikr.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ZikrUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Zikr.objects.all()
    serializer_class = ZikrSerializer


class ZikrDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Zikr.objects.all()
    serializer_class = ZikrSerializer

class IncrementZikrCountView(UpdateAPIView):
    queryset = Zikr.objects.all()
    serializer_class = ZikrSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.count_val >= instance.count-1:
            instance.count_val = 0
            instance.save()
        else:
            instance.count_val += 1

        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)