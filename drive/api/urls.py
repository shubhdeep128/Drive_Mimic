from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.FileView, base_name='Files')
urlpatterns = router.urls