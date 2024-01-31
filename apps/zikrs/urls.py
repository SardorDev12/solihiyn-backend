from django.urls import path
from .views import ZikrListCreateAPIView, ZikrUpdateAPIView, ZikrDeleteAPIView,IncrementZikrCountView

app_name = 'zikrs'

urlpatterns = [
    path('zikrs/', ZikrListCreateAPIView.as_view(), name="zikrs"),
    path('zikrs/update/<int:pk>/', ZikrUpdateAPIView.as_view(), name="zikr update"),
    path('zikrs/update/<int:pk>/inc/', IncrementZikrCountView.as_view(), name="zikr delete"),
    path('zikrs/delete/<int:pk>/', ZikrDeleteAPIView.as_view(), name="zikr delete"),
]