from django.contrib import admin
from .models import File
from . models import *
# Register your models here.


admin.site.register(File)



# class FileAdmin(admin.ModelAdmin):
#     # list_display = ('name','upload_file','timestamp','uploader')
#     # actions = None

#     # def save_model(self, request, obj, form, change):
#     #     if not obj.uploader:
#     #         obj.uploader = request.user
#     #     obj.save()
#     exclude=['uploader',]