from django.shortcuts import render
from .models import File
from django.views.generic.edit import CreateView,UpdateView,DeleteView 
from django.urls import reverse_lazy
from .serializers import FileSerializer
from rest_framework import viewsets, generics





