from rest_framework import serializers

class PrestamoTotalSerializer(serializers.Serializer):
    prestamosPorDia = serializers.ListField(
        child=serializers.FloatField(min_value=0),
        allow_empty=False
    )
