from rest_framework import serializers

class ControlPesoSerializer(serializers.Serializer):
    pesoActual = serializers.FloatField(min_value=0)
    pesoIdeal = serializers.FloatField(min_value=0)
