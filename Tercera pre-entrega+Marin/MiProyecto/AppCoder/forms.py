from django import forms
from .models import Categoria, Producto, Cliente

class CategoriaForm(forms.ModelForm):
    OPCIONES_CATEGORIA = [
        ('camaras', 'Cámaras'),
        ('alarma', 'Alarma'),
        ('dvr', 'DVR'),
    ]

    nombre = forms.ChoiceField(choices=OPCIONES_CATEGORIA, label='Categoría')

    class Meta:
        model = Categoria
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio']

class ClienteSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)
