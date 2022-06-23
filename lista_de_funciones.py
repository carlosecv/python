def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3


funciones = [cuadrado, cubo]

enteros = [1, 2, 4, 7]

import pdb;pdb.set_trace()
for e in enteros:
    valores = list(map(lambda x : x(e), funciones))
    print(valores)