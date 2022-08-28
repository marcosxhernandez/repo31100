class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print(f"hola, me llamo {self.nombre} {self.apellido} y tengo {self.edad} anos")