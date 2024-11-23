class Estudiante:
    def _init_(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.materias = []

    def inscribir_materia(self, materia):
        self.materias.append(materia)

    def mostrar_materias(self):
        print(f"Materias inscritas por {self.nombre}: {', '.join(self.materias)}")

    def actualizar_grado(self, nuevo_grado):
        self.grado = nuevo_grado

# Ejemplo de uso
estudiante1 = Estudiante("Juan", 15, "10°")
estudiante2 = Estudiante("Ana", 14, "9°")
estudiante3 = Estudiante("Carlos", 16, "11°")

estudiante1.inscribir_materia("Matemáticas")
estudiante1.inscribir_materia("Ciencias")
estudiante1.mostrar_materias()
estudiante1.actualizar_grado("11°")