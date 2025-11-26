# catalog/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from mascotas.views.mascota import mascotaViewSet
from mascotas.views.control_peso import ControlPesoView


router = DefaultRouter()
router.register(r'mascotas', mascotaViewSet, basename='mascota')

urlpatterns = [
    path('mascotas/control-peso', ControlPesoView.as_view(), name='control-peso'),
] + router.urls
