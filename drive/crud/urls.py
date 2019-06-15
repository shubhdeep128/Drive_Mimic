from . import views
from django.conf.urls import url
from django.urls import path,include
from rest_framework import routers

app_name = 'crud'


urlpatterns=[
    path('',views.FileList.as_view()),
    path('<int:pk>',views.FileDetail.as_view())
  
]