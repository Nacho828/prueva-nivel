class Bicicleta:
    def __init__(self, color, marca, tipo, ruedas):
        self.color = color
        self.marca = marca
        self.tipo = tipo
        self.ruedas = ruedas

    def __str__(self):
        return f"Bicicleta(color={self.color}, marca={self.marca}, tipo={self.tipo}, ruedas={self.ruedas})"
    
    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print (f"(vehiculo.__name__.__class__)):{vehiculo}")