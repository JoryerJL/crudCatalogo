from django.shortcuts import render, redirect
from productos.models import *
from .forms import *

# Create your views here.
def index_dashboard(request):
    productos = Producto.objects.all
    context = {
        'title': 'Dashboard',
        'productos': productos
    }
    return render(request, 'dashboard/index.html', context)

def create_producto(request):
    form = ProductoCreateForm()
    if request.method == 'POST':
        form = ProductoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:index')
        else:
            print(form.errors)
    context = {
        'title': 'Crear Producto',
        'form': form
    }
    return render(request, 'dashboard/createProducto.html', context)

def delete_producto(request, pk):
    Producto.objects.get(id=pk).delete()
    return redirect('dashboard:index')

def update_product(request, pk):
    producto = Producto.objects.get(id=pk)
    form = ProductoCreateForm(instance=producto)
    if request.method == 'POST':
        form = ProductoCreateForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('dashboard:index')
        else:
            print(form.errors)
    context = {
        'title': 'Actualizar Producto',
        'form': form
    }
    return render(request, 'dashboard/createProducto.html', context)

def detail_product(request, pk):
    producto = Producto.objects.get(id=pk)
    context = {
        'title': 'Detalle del Producto',
        'producto': producto
    }
    return render(request, 'dashboard/detailProducto.html', context)