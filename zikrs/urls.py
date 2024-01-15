from django.urls import path
from .views import ZikrListCreateAPIView, ZikrUpdateAPIView, ZikrDeleteAPIView

app_name = 'zikrs'

urlpatterns = [
    path('zikrs/', ZikrListCreateAPIView.as_view(), name="zikrs"),
    path('zikrs/update/<int:pk>', ZikrUpdateAPIView.as_view(), name="zikr update"),
    path('zikrs/delete/<int:pk>', ZikrDeleteAPIView.as_view(), name="zikr delete"),
]