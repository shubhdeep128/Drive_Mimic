from rest_framework import serializers, exceptions
from crud.models import File
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User
#uploader=get_user_model()

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        
        fields=('id','upload_file','uploader','name','timestamp')
        read_only_fields = ['id', 'uploader']
        model = File
        

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):
        username= data.get("username","")
        password=data.get("password","")

        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data["user"]=user
                else:
                    msg="Account Disabled"
                    raise exceptions.ValidationError(msg)
            else:
                msg="Invalid Credentials"
                raise exceptions.ValidationError(msg)

        else:
            msg="Please provide Username and Password"
            raise exceptions.ValidationError(msg)
        return data
    
