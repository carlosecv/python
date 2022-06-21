def es_par(numero):
    
    if numero % 2 == 0:
        return True
    else:
        return False

def es_o_no_es(numero):
    
    if es_par(numero):
        print("Es par")
    else:
        print("NO ES PAR !!!!")

es_o_no_es(2)
es_o_no_es(5)
es_o_no_es(89.456)
es_o_no_es(101)
es_o_no_es(-5)
es_o_no_es(-4)
