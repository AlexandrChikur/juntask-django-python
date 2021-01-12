from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from .models import User
from cars.serializers import CarsListSerializer

class UsersListSerializer(serializers.ModelSerializer):
    """Список всех пользователей """

    class Meta:
        model = User
        fields = ("name", "email", "lang")


class UserDetailSerializer(serializers.ModelSerializer):
    """Данные о пользователе """

    personal_cars = CarsListSerializer(many=True)

    class Meta:
        model = User
        fields = ("name", "email", "lang", "personal_cars")


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ("username", "email", "password", )