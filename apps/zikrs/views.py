from rest_framework.permissions import IsAuthenticated

from .serializers import ZikrSerializer
from .models import Zikr
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import RetrieveDestroyAPIView

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