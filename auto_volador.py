
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


vocho = Automovil("Rojo",60)
vochovolador= CocheVolador("Azul",35)

print(vochovolador.llantas)
print(vocho.llantas)

vocho.acelera()
vochovolador.acelera()

print(vochovolador.velocidad)
print(vocho.velocidad)

print("Puertas Coche Volador: %d" % vochovolador.puertas)

print("Esta Volando el Vocho Volador: %s" % vochovolador.esta_volando)

#vocho.vuela()
vochovolador.vuela()
print("Esta Volando el Vocho Volador: %s" % vochovolador.esta_volando)
#print("Esta Volando el Vocho: %s" % vocho.esta_volando)




