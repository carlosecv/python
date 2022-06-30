
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



# c1 = Automovil('rojo', 20)
# c2 = Automovil('blanco', 35)

# print(c1.color)
# print(c2.color)


# c1.acelera()

# c2.acelera()

# print(c1.velocidad)

# print(c2.velocidad)

# c1.acelera()
# c2.acelera()

# print(c1.velocidad)
# print(c2.velocidad)

# c1.aceleracion=90
# c1.aceleracion=60

# c1.acelera()
# c2.acelera()

# print(c1.velocidad)
# print(c2.velocidad)

