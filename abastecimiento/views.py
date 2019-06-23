from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Producto,Proveedor,Compra
from django.forms import formsets, formset_factory
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'ventas/menu2.html')





class ProductoList(ListView):
    model = Producto
    paginate_by = 20
    template_name = 'abastecimiento/productos.html'





class CrearCompra(CreateView):
    pass
    


class ListadoCompras(ListView):
    model = Compra
    template_name = 'abastecimiento/compras.html'
    context_object_name = 'compras'

