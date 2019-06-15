from rest_framework import serializers
from crud import models



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','upload_file','name','timestamp')
        model = models.File