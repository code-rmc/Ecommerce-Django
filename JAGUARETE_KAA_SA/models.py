from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80)

    def __str__(self):
        return self.descripcion


class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    imagen = models.ImageField(upload_to="productos")
    descripcion = models.CharField(max_length=200)  # CAMBIAR A TEXTFIELD
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


# class Carrito(models.Model):
#     id = models.AutoField(primary_key=True)
#     usuario = models.ForeignKey(
#         User, on_delete=models.CASCADE
#     )  # REALACION CON TABLA USUARIO
#     lista_productos = models.ManyToManyField(
#         Productos, blank=True, on_delete=models.CASCADE
#     )
#     total_carrito = models.DecimalField(max_digits=6, decimal_places=2)

#     def __str__(self):
#         return f"Usuario: {self.usuario}"
