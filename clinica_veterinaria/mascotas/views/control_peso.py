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
        
        peso_actual = serializer.validated_data['pesoActual']
        peso_ideal = serializer.validated_data['pesoIdeal']
        
        # Calcular la diferencia
        diferencia = peso_actual - peso_ideal
        
        # Determinar el mensaje según la diferencia
        if diferencia > 0:
            mensaje = "La mascota está por encima del peso ideal"
        elif diferencia < 0:
            mensaje = "La mascota está por debajo del peso ideal"
        else:
            mensaje = "Peso ideal alcanzado"
        
        return Response({
            "diferencia": diferencia,
            "mensaje": mensaje
        }, status=status.HTTP_200_OK)
