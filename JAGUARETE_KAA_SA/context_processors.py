from .models import Categoria


def categoriaMenu(request):
    categoriaMenu = Categoria.objects.all()
    return {"categorias": categoriaMenu}
