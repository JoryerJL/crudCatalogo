from django.forms import ModelForm
from productos.models import *

class ProductoCreateForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'