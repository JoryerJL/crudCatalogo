from django.contrib import admin
from productos.models import *

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Imagenes)