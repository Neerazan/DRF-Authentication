from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes

from .models import *
from .serializers import *

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key
            })
        else:
            return Response({
                'error': 'Invalid Chredentials'
            },
            status=401
            )


@api_view(['get'])
@permission_classes([permissions.IsAuthenticated])
def say_hello(request):
    # print(request.body)
    return render(request, 'hello.html', {
        'name': 'hello world'
    })