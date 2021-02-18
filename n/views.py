from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *
class TrackViewSet(viewsets.ModelViewSet):
    queryset=Track.objects.all()
    serializer_class = TrackSerializer
class AlbumViewSet(viewsets.ModelViewSet):
    queryset=Album.objects.all()
    serializer_class = AlbumSerializer

# Create your views here.
