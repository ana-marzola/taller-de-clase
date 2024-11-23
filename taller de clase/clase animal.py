class Animal:
    def _init_(self, nombre, especie, edad, habitat):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.habitat = habitat

    def cumplir_años(self):
        self.edad += 1

    def cambiar_habitat(self, nuevo_habitat):
        self.habitat = nuevo_habitat

    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}, Hábitat: {self.habitat}")

# Ejemplo de uso
animal1 = Animal("Leo", "León", 5, "Sabana")
animal2 = Animal("Manny", "Elefante", 10, "Selva")
animal1.mostrar_detalles()
animal1.cumplir_años()
animal1.cambiar_habitat("Zoológico")
animal1.mostrar_detalles()