from superclases.vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} cc".format
    
    
    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print (f"(vehiculo.__name__.__class__)):{vehiculo}")

# Output: