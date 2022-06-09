#¿Qué es un Diccionario de datos?
#Un Diccionario es una estructura de datos y un tipo de dato en Python con características especiales 
# que nos permite almacenar cualquier tipo de valor como enteros, 
# cadenas, listas e incluso otras funciones. 
# Estos diccionarios nos permiten además identificar cada elemento por una clave (Key).

#Para definir un diccionario, se encierra el listado de valores entre llaves. Las parejas de clave y valor se separan con comas, y la clave y el valor se separan con dos puntos.

diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }

print(diccionario)

print(diccionario['nombre'])

print(diccionario['edad'])

print(diccionario['cursos'])
print(diccionario['cursos'][0])
print(diccionario['cursos'][1])
print(diccionario['cursos'][2])