from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    name=models.CharField(max_length=50, verbose_name="Nombre")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="categoria"
        verbose_name_plural="categorias"
    
    def __str__(self):
        return self.name
    
class PaquetePermit(models.Model):
    title=models.CharField(max_length=50, verbose_name="Titulo")
    descrip=models.TextField(verbose_name="Descripción")
    apertura=models.DateTimeField(default=now, verbose_name="Fecha de inicio disponibilidad")
    imagen=models.ImageField(upload_to="ejemplos", null=True, blank=True, verbose_name="Imagen")
    aprobador=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Aprobador")
    etiquetas=models.ManyToManyField(Etiqueta, verbose_name="Etiquetas")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="PaquetePermitido"
        verbose_name_plural="PaquetesPermitidos"
    
    def __str__(self):
        return self.name