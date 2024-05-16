from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]