# sensor urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('api', api_post_sensor),
]
