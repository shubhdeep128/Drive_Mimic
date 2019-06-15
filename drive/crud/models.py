from django.db import models
from django.urls import reverse


class File(models.Model):
    name=models.CharField(max_length=250)
    upload_file=models.FileField(blank=False, null=False)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)+'-'+str(self.timestamp)
# Create your models here.
