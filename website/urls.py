from django.urls import path, include
from .views import *

app_name = 'website'

urlpatterns = [
    path('', index, name='index'),
]