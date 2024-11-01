from lib2to3.fixes.fix_input import context
from productos.models import *

from django.shortcuts import render

# Create your views here.
def index(request):
    productos = Producto.objects.all()
    context = {
        'title': 'Principal',
        'productos': productos
    }
    return render(request, 'website/index.html', context)

def detalle_producto (request, pk):
    producto = Producto.objects.get(id=pk)
    context = {
        'title': 'Detalle del Producto',
        'producto': producto
    }
    return render(request, 'website/detalle.html', context)
