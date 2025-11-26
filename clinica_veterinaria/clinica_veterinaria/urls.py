# billing_api/urls.py (añadir catálogo)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include('users.urls')),   
  path('api/', include('mascotas.urls')),
  path('api/tratamientos/', include('tratamientos.urls')),
]
