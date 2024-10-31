from django.urls import path, include
from website.urls import app_name
from .views import *

app_name = 'dashboard'

urlpatterns = [
    path('', index_dashboard, name='index'),
    path('create/', create_producto, name='create'),
    path('delete/<int:pk>/', delete_producto, name='delete'),
]