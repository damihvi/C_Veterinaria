# catalog/serializers/category.py
from rest_framework import serializers
from mascotas.models import mascota

class mascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = mascota
        fields = ("id","nombre","especie","raza","color","fecha_nacimiento","peso_kg","nombre_duenio","telefono_duenio","email_duenio","is_active","created_at","updated_at")
        read_only_fields = ("id","created_at","updated_at")
