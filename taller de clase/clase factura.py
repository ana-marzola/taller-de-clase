
class Factura:
    def _init_(self, numero, cliente, fecha):
        self.numero = numero
        self.cliente = cliente
        self.fecha = fecha
        self.monto_total = 0
        self.items = []

    def agregar_item(self, descripcion, cantidad, precio_unitario):
        total_item = cantidad * precio_unitario
        self.items.append((descripcion, cantidad, precio_unitario, total_item))
        self.monto_total += total_item

    def mostrar_detalles(self):
        print(f"Factura N°: {self.numero}, Cliente: {self.cliente}, Fecha: {self.fecha}")
        for item in self.items:
            print(f"{item[0]} - Cantidad: {item[1]}, Precio unitario: ${item[2]}, Total: ${item[3]}")
        print(f"Monto Total: ${self.monto_total:.2f}")

    def aplicar_descuento(self, porcentaje):
        self.monto_total -= self.monto_total * (porcentaje / 100)

# Ejemplo de uso
factura1 = Factura(1, "Juan Pérez", "2024-11-18")
factura1.agregar_item("Laptop", 1, 1200)
factura1.agregar_item("Ratón", 2, 25)
factura1.mostrar_detalles()
factura1.aplicar_descuento(10)
factura1.mostrar_detalles()