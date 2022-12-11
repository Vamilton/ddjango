from django.urls import path
from django.contrib import admin

from measurement.views import All_sensors, One_sensor, Measurements

urlpatterns = [
    path('sensors/', All_sensors.as_view()),
    path('sensors/<pk>/', One_sensor.as_view()),
    path('measurements/', Measurements.as_view()),
]
