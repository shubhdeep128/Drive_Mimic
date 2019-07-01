from django.db import models
from django.contrib.auth.models import User
from api.firebase import store


class File(models.Model):

    uploader = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    upload_file = models.FileField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)+'-'+str(self.uploader)

    def save(self, *args, **kwargs):
        super(File, self).save(*args, **kwargs)
        path = self.upload_file
        name = self.name
        store(name, path)

    @property
    def owner(self):
        return self.uploader

# Create your models here.
