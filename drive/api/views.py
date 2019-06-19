from rest_framework import viewsets, exceptions
from crud import models
from . import serializers
from rest_framework.views import APIView
from django.contrib.auth import login as djangologin,logout as djangologout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response 
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .firebase import store
# Create your views here.




class FileView(viewsets.ModelViewSet):

    permission_classes=[IsOwnerOrReadOnly,IsAuthenticated]
    def get_queryset(self, *args, **kwargs):
        return models.File.objects.all().filter(uploader=self.request.user)
  
            
    def perform_create(self, serializer):
        
        serializer.save(uploader=self.request.user)
        
    serializer_class = serializers.FileSerializer


class LoginView(APIView):
    def post(self,request):
        serializer=serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data["user"]
        djangologin(request,user)
        token, created= Token.objects.get_or_create(user=user)
        return Response ({"token":token.key},status=200)




class LogoutView(APIView):
    authentication_classes=(TokenAuthentication,)
    
    def post(self, request):
        djangologout(request)
        return Response(status=204)

