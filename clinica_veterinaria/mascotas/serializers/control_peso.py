from rest_framework import serializers

class ControlPesoSerializer(serializers.Serializer):
    dias_retraso = serializers.FloatField(min_value=0)
    multa_dia = serializers.FloatField(min_value=0)
