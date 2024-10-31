from django.shortcuts import render
from productos.models import *

# Create your views here.
def index_dashboard(request):
    productos = Producto.objects.all
    context = {
        'title': 'Dashboard',
        'productos': productos
    }
    return render(request, 'dashboard/index.html', context)
