#enteros = [1, 2, 4, 7]
#cuadrados = []
#for e in enteros:
#    cuadrados.append(e ** 2)     
#print(cuadrados)


enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x : x ** 2, enteros))
print(cuadrados)
