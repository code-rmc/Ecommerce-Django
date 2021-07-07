from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("acerca-de/", views.acerca, name="acerca"),
    ##############################################################################
    # BUSQUEDA #
    ##############################################################################
    path("busqueda/<int:id>/", views.filtrarCategoria, name="filtrarCategoria"),
    path("busqueda/producto/", views.busquedaProducto, name="busquedaProducto"),
    ##############################################################################
    # PRODUCTOS #
    ##############################################################################
    path("producto/listar-producto/", views.listarProductos, name="listarProductos"),
    path("producto/nuevo/", views.nuevoProducto, name="nuevoProducto"),
    path(
        "producto/modificar/<int:id>/",
        views.modificarProducto,
        name="modificarProducto",
    ),
    path("producto/detalle/<int:id>/", views.detalleProducto, name="detalleProducto"),
    path("producto/<int:id>/", views.borrarProducto, name="borrarProducto"),
    ##############################################################################
    # CATEGORIA #
    ##############################################################################
    path("categoria/lista-categoria/", views.listarCategoria, name="listarCategorias"),
    path(
        "categoria/modificar/<int:id>/",
        views.modificarCategoria,
        name="modificarCategoria",
    ),
    path("categoria/borrar/<int:id>/", views.borrarCategoria, name="borrarCategoria"),
    ##############################################################################
    # CARRITO #
    ##############################################################################
    path("carrito/", views.carroProductos, name="carrito"),
    ##############################################################################
    # LOGIN Y REGISTRO #
    ##############################################################################
    path("login/", LoginView.as_view(template_name="login/login.html"), name="login"),
    path(
        "logout/", LogoutView.as_view(template_name="login/logout.html"), name="logout"
    ),
    path("registro/", views.registro, name="registro"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
