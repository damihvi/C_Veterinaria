# catalog/serializers/category.py
from rest_framework import serializers
from mascotas.models import mascota

class mascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = mascota
        fields = ("id","isbn","titulo","autor","editorial","anio_publicacion","categoria","num_paginas","ubicacion","estado","copias_disponibles")
        read_only_fields = ("id")
