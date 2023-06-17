from django.db import models

# Create your models here.
class Articulo(models.Model):
    tittle = models.CharField(max_length=150)
    description = models.TextField(max_length=360, null=True)
    tags = models.CharField(max_length=400, null=True)
    url = models.CharField(max_length=500)
    priority = models.FloatField(default=0.5)
    content = models.TextField(max_length=5000)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    create = models.DateField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    alt_image = models.CharField(max_length=150, null=True)
    autor = models.CharField(max_length=200, default='Estuardo Ramírez')
    visits = models.IntegerField(default=0, verbose_name="Total Visitas", null=True) 
    status = models.BooleanField(default=True, verbose_name="Estado")  

    class Meta:
        db_table = "Articulo"
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self) -> str:
        return self.tittle + " ID: " + str(self.id)
    
    def real_url(self) -> str:
        return f"http://estuardodev.com{self.url}/{self.id}"
    
    def real_url_image(self) -> str:
        return f"http://estuardodev.com/media/{self.image}"