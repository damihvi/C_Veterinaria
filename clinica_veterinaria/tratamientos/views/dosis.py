from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from tratamientos.serializers import PrestamoTotalSerializer

class prestamoTotalView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = PrestamoTotalSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        prestamosPorDia = serializer.validated_data['prestamosPorDia']
        
        # Calcular la suma total usando un ciclo
        prestamo_total = 0
        for prestamo in prestamosPorDia:
            prestamo_total += prestamo
        
        promedio_prestamos = prestamo_total / 7
        
        # Determinar el mensaje según la dosis total
        if prestamo_total < 100:
            mensaje = "“Poca actividad de préstamo"
        elif 100 <= prestamo_total <= 300:
            mensaje = "Actividad normal"
        else:
            mensaje = "Alta demanda de libros"
        
        return Response({
            "prestamoTotal": prestamo_total,
            "promedio": promedio_prestamos,
            "mensaje": mensaje
        }, status=status.HTTP_200_OK)
