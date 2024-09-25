from rest_framework import viewsets
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        users = User.objects.all()
        return Response({"users": [user.username for user in users]}, status=status.HTTP_200_OK)

    def create(self, request):
        user = User.objects.create_user(**request.data)
        return Response({"username": user.username}, status=status.HTTP_201_CREATED)
