from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from tratamientos.serializers import DosisTotalSerializer

class DosisTotalView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = DosisTotalSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        dosis_diarias = serializer.validated_data['dosisDiarias']
        
        # Calcular la suma total usando un ciclo
        dosis_total = 0
        for dosis in dosis_diarias:
            dosis_total += dosis
        
        # Determinar el mensaje según la dosis total
        if dosis_total < 100:
            mensaje = "Tratamiento de baja intensidad"
        elif 100 <= dosis_total <= 300:
            mensaje = "Tratamiento moderado"
        else:
            mensaje = "Tratamiento fuerte, seguir observación"
        
        return Response({
            "dosisTotal": dosis_total,
            "mensaje": mensaje
        }, status=status.HTTP_200_OK)
