import json
import uuid
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

from django.core.files.storage import default_storage
import csv
from ..models import *
from ..serializers import *


from rest_framework.pagination import PageNumberPagination

class WelcomeView(APIView):
    def get(self, request):
        return Response("Companies Info")


class RegisterView(APIView):
    def get(self, request):
        try:
            queryset = User.objects.all()
            serializer_class = UserSerializer(queryset, many=True)
            return Response(serializer_class.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # refresh = RefreshToken.for_user(user)
            return Response({"pass":"pass"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    