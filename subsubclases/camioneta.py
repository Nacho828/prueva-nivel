from subclase.coche import Coche

class Camionta(Coche):
    def __init__(self, marca, modelo, año,peso):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.peso = peso

    def descripcion(self):
        return f"{self.marca} {self.modelo} del año {self.año}"

    def descripcion(self):
        return f"{self.marca} {self.modelo} del año {self.año} con un peso de {self.peso} kg"

    def catalogar(self):
        if self.ruedas >= 4 :
            return "camioneta"
        else:
            return super