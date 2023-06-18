from django.db import models

# Create your models here.
class Portafolio(models.Model):
    '''Aqui se almacena información de mi portafolio'''
    imagen = models.CharField(max_length=50, null=True, verbose_name="Imágen")
    texto_largo = models.TextField(max_length=2000, null=False, verbose_name="Texto Largo")

    class Meta:
        verbose_name = "Portafolio"
        verbose_name_plural = "Portafolio"

    def __str__(self) -> str:
        return "Acerca De"
    
class Habilidades(models.Model):  
    descHabilidad = models.CharField(max_length=100, null=False, verbose_name="Habilidad")

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self) -> str:
        return self.descHabilidad
    
class Certificaciones(models.Model):
    imagen = models.CharField(max_length=50, null=True, verbose_name="Imágen") 
    titulo = models.CharField(max_length=50, null=False, verbose_name="Título") 
    descripcion = models.CharField(max_length=230, null=False, verbose_name="Descripción")
    enlace = models.URLField(max_length=255, null=False, verbose_name="Enlace")

    class Meta:
        verbose_name = "Certificaciones"
        verbose_name_plural = "Certificaciones"

    def __str__(self) -> str:
        return self.titulo
    
class Proyectos(models.Model):
    titulo = models.CharField(max_length=50, null=True, verbose_name="Título") 
    descripcion = models.CharField(max_length=230, null=True, verbose_name="Descripción")
    imagen = models.CharField(max_length=50, null=True, verbose_name="Imágen") 
    texto_enlace = models.CharField(max_length=50, null=True, verbose_name="Texto del Enlace")
    enlace = models.URLField(max_length=255, null=True, verbose_name="Enlace")
    alt_imagen = models.CharField(max_length=50, null=True, verbose_name="Alt Imagen")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self) -> str:
        return self.titulo