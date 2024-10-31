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
