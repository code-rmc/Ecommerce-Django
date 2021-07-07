from django.core.files.base import File
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import Categoria, Productos
from .forms import ProductosForm, CategoriaForm

# Create your views here.


def index(request):
    contexto = {
        "productos": Productos.objects.all()[:3],
        "listaProductos": Productos.objects.all()[3:13],
    }
    return render(request, "home/index.html", contexto)


def filtrarCategoria(request, id):
    contexto = {"productos": Productos.objects.filter(categoria=id)}
    return render(request, "home/categorias.html", contexto)


def busquedaProducto(request):
    productos = Productos.objects.filter(
        Q(titulo__icontains=request.GET.get("buscar"))
        | Q(descripcion__icontains=request.GET.get("buscar"))
    )
    return render(request, "home/categorias.html", {"productos": productos})


def acerca(request):
    return render(request, "home/acerca_de.html")


def detalleProducto(request, id):
    return render(
        request, "home/detalle.html", {"producto": Productos.objects.get(id=id)}
    )


@login_required(login_url="/login/")
def carroProductos(request):
    return render(request, "carro/carro_productos.html")


################
# REGISTRO DE USUARIOS
def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Usuario {username} Creado!!!")
            return redirect(to="index")
        else:
            messages.error(request, "Ocurrio un Error")
            form = UserCreationForm()
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "login/registro.html", context)


################
# ALTA PRODUCTOS
@login_required(login_url="/login/")
@permission_required("polls.add_choice", raise_exception=True)
def nuevoProducto(request):
    data = {"form": ProductosForm()}
    if request.method == "POST":
        formulario = ProductosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Guardado!!!")
        else:
            messages.error(request, "Ocurrio un Error")
            data["form"] = formulario
    return render(request, "productos/alta_productos.html", data)


################
# MODIFICAR PRODUCTOS
@login_required(login_url="/login/")
@permission_required("polls.add_choice", raise_exception=True)
def modificarProducto(request, id):
    producto = get_object_or_404(Productos, id=id)
    data = {"form": ProductosForm(instance=producto)}
    if request.method == "POST":
        formulario = ProductosForm(
            data=request.POST, instance=producto, files=request.FILES
        )
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Modificado")
            return redirect(to="listarProductos")
        data["form"] = formulario
        messages.error(request, "Ocurrio un Error")
    return render(request, "productos/mod_productos.html", data)


################
# LISTAR PRODUCTOS
@login_required(login_url="/login/")
@permission_required("polls.add_choice", raise_exception=True)
def listarProductos(request):
    return render(
        request,
        "productos/listar_productos.html",
        {"productos": Productos.objects.all()},
    )


################
# BORRAR PRODUCTOS
@login_required(login_url="/login/")
@permission_required("polls.add_choice", raise_exception=True)
def borrarProducto(request, id):
    producto = get_object_or_404(Productos, id=id)
    producto.delete()
    messages.success(request, "Producto Eliminado")
    return redirect(to="listarProductos")


################
# MODIFICAR CATEGORIA
@login_required(login_url="/login/")
@permission_required("polls.add_choice", raise_exception=True)
def modificarCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    data = {"form": CategoriaForm(instance=categoria)}
    if request.method == "POST":
        formulario = CategoriaForm(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Categoria Modificada")
            return redirect(to="listarCategorias")
        data["form"] = formulario
        messages.error(request, "Ocurrio un Error")
    return render(request, "categorias/alta_lista_categoria.html", data)


################
# LISTAR CATEGORIA
@login_required(login_url="/login/")
@permission_required("polls.add_choice", raise_exception=True)
def listarCategoria(request):
    data = {"categorias": Categoria.objects.all(), "form": CategoriaForm()}
    if request.method == "POST":
        formulario = CategoriaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Categoria Nueva!!!")
        else:
            data["form"] = formulario
            messages.error(request, "Ocurrio un Error")
    return render(request, "categorias/alta_lista_categoria.html", data)


################
# BORRAR CATEGORIA
@login_required(login_url="/login/")
@permission_required("polls.add_choice", raise_exception=True)
def borrarCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, "Categoria Eliminada")
    return redirect(to="listarCategorias")
