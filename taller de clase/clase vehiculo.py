class Vehiculo:
    def _init_(self, marca, modelo, año, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def conducir(self, km):
        self.kilometraje += km

    def mostrar_detalles(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje} km")

    def es_vehiculo_antiguo(self):
        return 2024 - self.año > 20

# Ejemplo de uso
vehiculo1 = Vehiculo("Toyota", "Corolla", 2000, 120000)
vehiculo2 = Vehiculo("Honda", "Civic", 2015, 80000)
vehiculo3 = Vehiculo("Ford", "Fiesta", 1995, 150000)

vehiculo1.mostrar_detalles()
print("Es antiguo:", vehiculo1.es_vehiculo_antiguo())
vehiculo1.conducir(100)
vehiculo1.mostrar_detalles()