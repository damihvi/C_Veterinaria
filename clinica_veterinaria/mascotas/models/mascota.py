from django.db import models

class mascota(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    especie = models.CharField(max_length=120)
    raza = models.CharField(max_length=120)
    color = models.CharField(max_length=120)
    fecha_nacimiento = models.DateTimeField()
    peso_kg = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_duenio = models.CharField(max_length=120)
    telefono_duenio = models.CharField(max_length=15)
    email_duenio = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return self.nombre