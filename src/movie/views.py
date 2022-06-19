from functools import partial
from rest_framework import (viewsets, status, permissions)
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import (SearchFilter, OrderingFilter)
from rest_framework.permissions import IsAdminUser
from knox.auth import TokenAuthentication
from rest_framework.decorators import action
from .serializers import (MovieSerializer, ShowsSerializer, SeatSerializer)
from .models import (Movie, Seat, Shows)
SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class MyPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS):
            return True
        return False


class MovieViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (MyPermission,)
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    print(queryset)
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title','cast__name']
    ordering_fields = ['popularity_index']
    ordering = ['-popularity_index']


class ShowsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (MyPermission,)
    serializer_class = ShowsSerializer
    queryset = Shows.objects.all().order_by('date','show_time')


class TicketBooking(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (MyPermission,)
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()
    @action(detail=False, methods=['post'], url_path='book-ticket')
    def book_ticket(self, request, **kwargs):
        serializer = SeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(booked_by_customer=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)