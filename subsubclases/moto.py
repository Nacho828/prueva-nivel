from subclase.bicicleta import Bicicleta


class Moto(Bicicleta):
    def __init__(self, color, ruedas, marca, tipo, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.marca = marca
        self.tipo = tipo
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Moto({self.color}, {self.ruedas} ruedas, {self.marca}, {self.tipo}, {self.cilindrada}cc)"
    
    def catalogar(vehiculos):    
        for vehiculo in vehiculos:
            print (type(vehiculo).__name__, vehiculo)