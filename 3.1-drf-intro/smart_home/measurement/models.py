from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Датчик')
    about = models.CharField(max_length=250, verbose_name='Какой')
    when = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.name



class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Датчик')
    temperature = models.IntegerField(verbose_name='Температура')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    image = models.ImageField(blank=True, verbose_name='Фото')
