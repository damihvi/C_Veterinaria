from rest_framework import serializers

class DosisTotalSerializer(serializers.Serializer):
    dosisDiarias = serializers.ListField(
        child=serializers.FloatField(min_value=0),
        allow_empty=False
    )
