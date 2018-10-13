from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Inmate
from .serializers import InmateSerializer

class InmateView(viewsets.ModelViewSet):
    queryset = Inmate.objects.all()
    
    serializer_class = InmateSerializer
