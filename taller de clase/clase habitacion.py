class Habitacion:
    def _init_(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada.")
        else:
            print(f"Habitación {self.numero} no está disponible.")

    def liberar(self):
        self.disponible = True
        print(f"Habitación {self.numero} está ahora disponible.")

    def mostrar_informacion(self):
        print(f"Habitación {self.numero}, Tipo: {self.tipo}, Precio: ${self.precio}, Disponible: {self.disponible}")

# Ejemplo de uso
habitacion1 = Habitacion(101, "Sencilla", 50)
habitacion2 = Habitacion(102, "Doble", 80)
habitacion3 = Habitacion(103, "Suite", 150)

habitacion1.mostrar_informacion()
habitacion1.reservar()
habitacion1.liberar()