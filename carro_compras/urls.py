from django.urls import path
from . import views

app_name = "carro_compras"

urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregarCarro, name="agregarCarro"),
    path("eliminar/<int:producto_id>/", views.eliminarCarro, name="eliminarCarro"),
    path("restar/<int:producto_id>/", views.restarCarro, name="restarCarro"),
    path("limpiarCarro/", views.limpiarCarro, name="limpiarCarro"),
]
