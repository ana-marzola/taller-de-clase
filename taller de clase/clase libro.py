class Libro:
    def _init_(self, titulo, autor, genero, precio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Precio: ${self.precio:.2f}")

    def es_mas_caro_que(self, otro_libro):
        return self if self.precio > otro_libro.precio else otro_libro

# Ejemplo de uso
libro1 = Libro("1984", "George Orwell", "Distopía", 15.0)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 18.0)
libro1.aplicar_descuento(10)
libro1.mostrar_informacion()
libro_mas_caro = libro1.es_mas_caro_que(libro2)
print("El libro más caro es:")
libro_mas_caro.mostrar_informacion()