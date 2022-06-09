#Listas
print('************** Listas *************')
lista = []
lista = list()

lista = ['hola','adios','que paso?','no paso','quien sabe']
print(lista)

# agregar elementos a una lista

lista.append('ke hubo?')
lista.append('hola ke hase?')
lista.append('no lo se')

print(lista)
# Iterar es ir pasando de elemento en elemento en un arreglo de principio a fin
# En Python, los tipos principales iterables son list, tuple, dict, set o string
# entre otros, son iterables, por lo que podran ser usados en el bucle for.

for a in lista:
    print(a)

# cambiar elementos a una lista

lista[5] = ' me cambiaron el texto!!!'

for a in lista:
    print(a)

#TUPLAS
print('************** Tuplas *************')
tupla = (6,7,8)

print(tupla)

for a in tupla:
    print(a)

#tupla[1]= 99999

print(tupla)


#tupla.append('a')
#tupla.add('a')

# conjunto
print('************** Conjuntos *************')
conjunto = {'hola','adios','que paso?','no paso','quien sabe'}

for c in conjunto:
    print(c)

conjunto.add('Este es otro texto agregado a mi conjunto')
conjunto.add('hola')
for c in conjunto:
    print(c)

#conjunto[2] = 'Perro consentido'
#print(conjunto[2]) 
print('adios' in conjunto)

i=0
for c in conjunto:    
    if c == 'que paso?':
        print(c)
        print(i)
    i+=1

#Diccionarios
print('************** Diccionarios *************')

diccionario = {
        'nombre' : 'Rogelio',
        'calle': 'Montenegro #45',
        'escolaridad': ['primaria','secundaria','preparatoria'],
        'edad': 45
}


print(diccionario)

#regresa una lista de tuplas donde cada tupla es la llave y el valor del diccionario
print(diccionario.items())

#transforma 2 iterables del mismo tamano enun diccionario llave: valor de cada elemento de cada iterable
dic = dict(zip('abcd',[1,2,3,4]))

print(dic)


#lista de llaves
print(diccionario.keys())


