from rest_framework import serializers
from .models import Zikr

class ZikrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zikr
        fields = '__all__'