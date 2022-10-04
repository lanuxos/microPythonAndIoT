# sensor urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('about/', About, name='about-page'),
    path('sensor/', SensorTable, name='sensor-page'),
    path('login/', Login, name='login-page'),
    path('api', api_post_sensor),
]
