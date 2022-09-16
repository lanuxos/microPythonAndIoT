from rest_framework import serializers
from .models import TempHumid

class TempHumidSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempHumid
        fields = ('id', 'code', 'title', 'temperature', 'humidity')