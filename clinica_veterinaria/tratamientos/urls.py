from django.urls import path
from tratamientos.views import prestamoTotalView

urlpatterns = [
    path('prestamo_total', prestamoTotalView.as_view(), name='prestamo_total'),
]
