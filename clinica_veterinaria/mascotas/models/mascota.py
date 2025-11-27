from django.db import models

class mascota(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=120)
    titulo = models.CharField(max_length=120)
    autor = models.CharField(max_length=120)
    editorial = models.CharField(max_length=120)
    anio_publicacion = models.DateTimeField()
    categoria = models.CharField(max_length=20,default="sin_categoria")
    num_paginas = models.PositiveIntegerField(default=0)
    ubicacion = models.CharField(max_length=15)
    estado = models.CharField(max_length=120)
    copias_disponibles = models.CharField(max_length=120)

    class Meta:
        ordering = ("isbn","titulo","autor","editorial","anio_publicacion","categoria","num_paginas","ubicacion","estado","copias_disponibles")

    def __str__(self):
        return self.isbn
    