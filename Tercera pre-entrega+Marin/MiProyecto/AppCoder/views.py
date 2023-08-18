from django.shortcuts import render
from .forms import CategoriaForm, ProductoForm, ClienteSearchForm
from .models import Categoria, Producto, Cliente

def insertar(request):
    categoria_form = CategoriaForm()
    producto_form = ProductoForm()

    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        producto_form = ProductoForm(request.POST)
        if categoria_form.is_valid() and producto_form.is_valid():
            categoria_form.save()
            producto_form.save()

    return render(request, 'insertar.html', {'categoria_form': categoria_form, 'producto_form': producto_form})

def buscar(request):
    search_form = ClienteSearchForm()
    results = []

    if request.method == 'POST':
        search_form = ClienteSearchForm(request.POST)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            results = Cliente.objects.filter(nombre__icontains=query)

    return render(request, 'buscar.html', {'search_form': search_form, 'results': results})
