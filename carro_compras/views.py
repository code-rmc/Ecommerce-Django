from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .carro import Carro
from JAGUARETE_KAA_SA.models import Productos

# Create your views here.


@login_required(login_url="/login/")
def agregarCarro(request, producto_id):
    carro = Carro(request)
    cantidad = request.GET.get("cantidad")
    if type(cantidad) == str:
        cantidad = int(cantidad)
    else:
        cantidad = 1
    producto = Productos.objects.get(id=producto_id)
    carro.agregar_carro(producto, cantidad)
    messages.success(request, f"Producto Agregado")
    return redirect("index")


@login_required(login_url="/login/")
def eliminarCarro(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.eliminar_carro(producto)
    messages.success(request, f"Producto eliminado")
    return redirect("index")


@login_required(login_url="/login/")
def restarCarro(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.restar_carro(producto)
    messages.success(request, f"A Quitado un Producto")
    return redirect("index")


@login_required(login_url="/login/")
def limpiarCarro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    messages.success(request, f"Todos los Productos fueron Eliminados")
    return redirect("index")
