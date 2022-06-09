a=9
b=15


#and
print("Operador and")
print(a>7 and b<20)
print(a>=9 and b<=20)
print(a!=b and b!=15)
print(a>b and b==15)

#or
print("Operador or")
print(a>7 or b<20)
print(a>=9 or b<=20)
print(a!=b or b!=15)
print(a>b or b==15)

#not
print("Operador not")
print(not (a>7 and b<20))
print(not (a>=9 and b<=20))
print(not (a!=b and b!=15))
print(not (a>b and b==15))

#Combinado
a=9
b=15
print("a=9")
print("b=15")
print("not a>b and b==15 or b+2<a")

print(not a>b and b==15 or b+2<a)
print ("Paso a Paso:")
print("a>b:")
print(a>b)
print("not a>b")
print(not a>b)
print("not a>b and b==15")
print(not a>b and b==15)
print("b==15:")
print(b==15)
print("b+2<a")
print(b+2<a)
print("True or False")
print(not a>b and b==15 or b+2<a)