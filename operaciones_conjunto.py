a = {'a','b','c','d'}

b = {'e','f','g','h','a'}

c = {'c','d','a','b',}

d = {'a','d'}

print(a == b)
print(a == c)

#B es un subconjunto de a?
print(d.issubset(a))
print(b.issubset(a))
#A es un superconjunto de d?
print(a.issuperset(d))


#Diferencia simetrica (UNION excluyedo los elementos iguales de cada conjunto)

a = {'a','b','c','d'}

b = {'e','f','g','h','a'}

f = a.symmetric_difference(b)
print(f)
