class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro

    def agregar_carro(self, producto, cantidad=1):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "imagen": producto.imagen.url,
                "nombre": producto.titulo,
                "precio": float(producto.precio) * cantidad,
                "cantidad": cantidad,
            }
        else:
            self.carro[str(producto.id)]["cantidad"] += cantidad
            self.carro[str(producto.id)]["precio"] = self.carro[str(producto.id)][
                "cantidad"
            ] * float(producto.precio)
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modifield = True

    def eliminar_carro(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()

    def restar_carro(self, producto):
        self.carro[str(producto.id)]["cantidad"] -= 1
        self.carro[str(producto.id)]["precio"] = self.carro[str(producto.id)][
            "cantidad"
        ] * float(producto.precio)
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modifield = True
