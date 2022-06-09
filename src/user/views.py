from time import time
from django.shortcuts import render
from .models import CustomUser, PasswordResetCode
from .serializers import LoginSerializer, UserMeSerializer, UserSerializer, ChangePasswordSerializer, PasswordResetSerializer, PasswordResetVerifiedSerializer
from knox.models import AuthToken
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from datetime import timedelta
from core.settings import *
from .models import f


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)[1]
        return Response({
            "token": token
        })
        
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = CustomUser.objects.filter(username=user)
        return queryset

    @action(detail=True, methods=['patch'], url_path='change-password')
    def change_password(self, request, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
            }

            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='password-reset')
    def password_reset(self, request, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        try:
            user = CustomUser.objects.get(email=email)
            PasswordResetCode.objects.send_mail(user)
            content = {'email': email}
            return Response(content, status=status.HTTP_201_CREATED)
        except Exception:
            print('CustomUser matching query does not exist')
        content = {'detail': ('Password reset not allowed.')}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['post'], url_path='password-reset-verified')
    def password_reset_verified(self, request, **kwargs):
        serializer = PasswordResetVerifiedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']
        password = serializer.validated_data['password']
        code = code.encode()
        code = f.decrypt(code)
        code = code.decode()
        splits = code.split(",")
        try:
            user = CustomUser.objects.get(email=splits[1])
            user.set_password(password)
            user.save()
            content = {'success': ('Password reset.')}
            return Response(content, status=status.HTTP_200_OK)
        except Exception:
            content = {'detail': ('Unable to verify user.')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
            
