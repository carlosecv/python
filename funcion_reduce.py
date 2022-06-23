# valores = [2, 4, 6, 5, 4]
# suma = 0
# for el in valores:
#     suma += el
# print(suma)

from functools import reduce
valores = [2, 4, 6, 5, 4]
suma = reduce(lambda x, y: x + y, valores)
print(suma)

