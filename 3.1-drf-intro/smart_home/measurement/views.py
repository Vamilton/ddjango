from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class All_sensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'Датчик': 'добавлен'})


class One_sensor(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        object = Sensor.objects.get(id=pk)
        serializer = self.serializer_class(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'Датчик': 'изменён'})

class Measurements(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class =MeasurementSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'Температура': [request.data['temperature']]})