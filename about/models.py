from django.db import models

# Create your models here.

class Team(models.Model):
    name=models.CharField(max_length=100, verbose_name='Nombre')
    lastname=models.CharField(max_length=100, verbose_name='Apellido')
    position=models.CharField(max_length=100, verbose_name='Cargo')
    image=models.ImageField(verbose_name='Imagen', upload_to="about")
    descript=models.TextField(verbose_name="Descripción",null=True, blank=True)
    urlFacebook=models.URLField(verbose_name='Enlace Facebook',null=True, blank=True)
    urlInstagram=models.URLField(verbose_name='Enlace Instagram',null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name='Creación')
    updated=models.DateTimeField(auto_now=True, verbose_name="Modificación")

    class Meta:
        verbose_name="Empleado"
        verbose_name_plural="Equipo de trabajo"
        ordering=["created"]

    def __str__(self):
        return self.name