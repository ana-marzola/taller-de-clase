class Producto:
    def _init_(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def ajustar_inventario(self, cantidad):
        self.cantidad += cantidad

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad}")

# Ejemplo de uso
producto1 = Producto("Manzana", 1.5, 100)
producto2 = Producto("Pan", 0.8, 50)
producto3 = Producto("Leche", 2.3, 30)

producto1.mostrar_informacion()
producto1.actualizar_precio(1.6)
producto1.ajustar_inventario(-10)
producto1.mostrar_informacion()