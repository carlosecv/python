
def tipo(edad):
    if edad < 0:
        return False
    if edad <=18:
        return "menor de edad"
    elif edad >=19 and edad < 60:
        return "Adulto"
    else:
        return "Adulto mayor"

name = input('Nombre: ')
edad = input('Que edad tienes: ')


print("Bienvenido %s, eres %s" % (name,tipo(int(edad))))

