
def muestra_x():
    x = 10
    global y
    y = 9
    print(f'x en la funcion vale {x}')
    print(f'y en la funcion vale {y}')
    
y = 20
muestra_x()
print(f'y fuera de la funcion vale {y}')