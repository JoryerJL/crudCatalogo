from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

class Imagenes (models.Model):
    imagen = models.ImageField()

    def __str__(self):
        return self.imagen.url

class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    imagen = models.ImageField()
    detalle = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    galeria = models.ManyToManyField(Imagenes, blank=True, null=True)


    def __str__(self):
        return self.nombre