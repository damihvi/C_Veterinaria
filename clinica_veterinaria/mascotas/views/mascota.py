# catalog/views/category.py
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from mascotas.models import mascota
from mascotas.serializers import mascotaSerializer
from mascotas.pagination import StandardResultsSetPagination

class mascotaViewSet(viewsets.ModelViewSet):
    queryset = mascota.objects.all()
    serializer_class = mascotaSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination 
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("nombre","slug")
    ordering_fields = ("id","nombre","especie","raza","color","slug","fecha_nacimiento","peso_kg","nombre_duenio","telefono_duenio","email_duenio","is_active","created_at","updated_at")
