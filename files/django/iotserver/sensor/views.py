from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from .serializers import TempHumidSerializer
from .models import *

def Home(request):
    context = {}
    return render(request, 'sensor/home.html', context)
def SensorTable(request):
    tempHumid = TempHumid.objects.all()
    temp = []
    humid = []
    for t in tempHumid:
        temp.append(t.temperature)
        humid.append(t.humidity)
    context = {'temp': temp, 'humid': humid, 'data': tempHumid}
    return render(request, 'sensor/sensor.html', context)
def About(request):
    return render(request, 'sensor/about.html')
def Login(request):
    return render(request, 'sensor/login.html')

@api_view(['POST'])
def api_post_sensor(request):
    print('Post data from esp32')

    if request.method == 'POST':
        ser = TempHumidSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)