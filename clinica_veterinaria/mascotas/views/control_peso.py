from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from mascotas.serializers.control_peso import ControlPesoSerializer

class ControlPesoView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = ControlPesoSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        dias_retraso = serializer.validated_data['dias_retraso']
        multa_dia = serializer.validated_data['multa_dia']
        
        # Calcular la diferencia
        multa = dias_retraso * multa_dia
        
        # Determinar el mensaje según la diferencia
        if multa <= 5:
            mensaje = "Retraso leve"
        elif 5 <= multa <= 15 :
            mensaje = "Retraso moderado"
        else:
            mensaje = "Retraso grave, revisar con administración"
        
        return Response({
            "dias_retraso":dias_retraso,
            "multa": multa,
            "mensaje": mensaje
        }, status=status.HTTP_200_OK)
