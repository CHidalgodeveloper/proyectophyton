from django.db import models
from about.models import Team

# Create your models here.
class Servicio(models.Model):
    service=models.CharField(max_length=100,verbose_name='Servicio')
    content=models.TextField(verbose_name='Contenido')
    image=models.ImageField(verbose_name='Imagen',upload_to="services")
    responsible=models.ManyToManyField(Team, verbose_name="Responsable")
    created=models.DateTimeField(auto_now_add=True,verbose_name='creado')
    updated=models.DateTimeField(auto_now=True,verbose_name='modificado')

    class Meta:
        verbose_name="Servicio"
        verbose_name_plural="Servicios"
        ordering=["created"]

    def __str__(self):
        return self.service
