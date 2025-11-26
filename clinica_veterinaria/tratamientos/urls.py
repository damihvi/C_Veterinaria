from django.urls import path
from tratamientos.views import DosisTotalView

urlpatterns = [
    path('dosis-total', DosisTotalView.as_view(), name='dosis-total'),
]
