def tabla_del(numero):
    resultados = []
    for i in range(11):
        resultados.append(numero * i)
    return resultados
 


for n in range(1,101):
    res = tabla_del(n)
    print(res)
