from .serializers import ZikrSerializer
from .models import Zikr
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import RetrieveDestroyAPIView

class ZikrListCreateAPIView(ListCreateAPIView):
    queryset = Zikr.objects.all()
    serializer_class = ZikrSerializer

class ZikrUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Zikr.objects.all()
    serializer_class = ZikrSerializer

class ZikrDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Zikr.objects.all()
    serializer_class = ZikrSerializer