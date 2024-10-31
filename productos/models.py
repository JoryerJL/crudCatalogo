from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    imagen = models.ImageField()


    def __str__(self):
        return self.nombre