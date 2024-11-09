from django.urls import path, include
from .views import *

app_name = 'registration'
urlpatterns = [
    path('logout/', logout_view, name='logout'),
]