# catalog/urls.py
from rest_framework.routers import DefaultRouter
from mascotas.views.mascota import mascotaViewSet


router = DefaultRouter()
router.register(r'mascotas', mascotaViewSet, basename='mascota')

urlpatterns = router.urls
