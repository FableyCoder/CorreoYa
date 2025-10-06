from django.db import models

# Create your models here.
class Reviews(models.Model):
    titulo=models.CharField(max_length=100)
    comentario=models.TextField()
    imagen=models.ImageField(upload_to="projects", verbose_name="Imagen")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

class Meta:
    verbose_name="Calificacion"
    verbose_name_plural="Calificaciones"

def __str__(self):
    return self.titulo