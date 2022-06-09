#Conjuntos: Arreglos con elementos que no se duplican

s = {1, 2, 3, 4}
print(s)

s = {1, 2, 3, 4, 4, 4, 5}
print(s)

#Agregamos elementos
s.add(5)
s.add(5)
s.add(6)

print(s)
#Quitar elementos
s.discard(2)
print(s)
s.discard(8)


print(s)

print(4 in s)

#Limpia un conjunto
s.clear()
print(s)

print("Otro ejercicio:")
s = set({6,7,8,9,2,3,1})
print(s)

s.discard(8)
print(s)

