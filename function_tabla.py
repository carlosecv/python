def tabla_del(numero):
    resultados = []
    for i in range(11):
        resultados.append(numero * i)
    return resultados
 

res = tabla_del(9)
print(res)


res = tabla_del(5)
print(res)
