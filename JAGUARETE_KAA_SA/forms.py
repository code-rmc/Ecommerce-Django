from django import forms
from django.forms import fields
from .models import Categoria, Productos

class ProductosForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = '__all__'

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'
