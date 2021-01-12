from rest_framework import serializers

from .models import Car

class CarsListSerializer(serializers.ModelSerializer):
    """ Получение автомобилей """    

    class Meta:
        model = Car
        exclude = ("owner", )