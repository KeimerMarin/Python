from django.urls import path
from . import views

urlpatterns = [
    path('insertar/', views.insertar, name='insertar'),
    path('buscar/', views.buscar, name='buscar'),
]
