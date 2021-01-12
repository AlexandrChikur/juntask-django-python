from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from cars.models import Car

from .serializers import UsersListSerializer, UserDetailSerializer


class UsersListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UsersListSerializer(users, many=True)
        return Response(serializer.data)


class UserDetailView(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
