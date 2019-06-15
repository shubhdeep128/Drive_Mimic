from django.shortcuts import render
from rest_framework import viewsets
from crud import models
from . import serializers

# Create your views here.

class FileView(viewsets.ModelViewSet):
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer