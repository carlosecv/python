
class Automovil:
    llantas = 4
    puertas = 4

    def __init__(self,color,aceleracion):
        self.color=color
        self.aceleracion=aceleracion
        self.velocidad=0
    

    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion
    
    def frena(self):
        v = self.velocidad - self.aceleracion
        if v < 0:
            v = 0
        self.velocidad = v



class CocheVolador(Automovil):
    llantas = 6
    def __init__(self, color, aceleracion, esta_volando=False):
        super().__init__(color, aceleracion)
        self.esta_volando = esta_volando

    def vuela(self):
        self.esta_volando = True

    def aterriza(self):
        self.esta_volando = False

class Anfibio(Automovil):
    sumergido = False

    def __init__(self, color, aceleracion, esta_en_agua=False):
        super().__init__(color, aceleracion)
        self.esta_en_agua = esta_en_agua
        

    def sumergirse(self):
        if self.esta_en_agua:
            self.sumergido = True
        else:
            print("El auto no esta en el agua y no se puede sumergir")
    def emerger(self):
        if self.sumergido:
            self.sumergido = False
        else:
            print("El auto no esta sumergido")

    def salir_del_agua(self):
        if self.esta_en_agua:
            self.esta_en_agua = False
        else:
            print("El auto no esta en el agua")