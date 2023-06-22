def soma (lista_numeros:list ) :
    total = 0
    for numero in lista_numeros:
        total += numero
    return total    


def subtracao (lista_numeros:list ) :
    total = lista_numeros[0]
    tamanho  = len (lista_numeros)
    while tamanho != 1:
        tamanho -=1
        total -= lista_numeros[tamanho] 
    return total    

def multiplicacao (lista_numeros:list ) :
    total = 1
    for numero in lista_numeros:
        total *= numero
    return total  

def divisao (lista_numeros:list ) :
    total = lista_numeros[0]
    tamanho  = len (lista_numeros)
    while tamanho != 1:
        tamanho -=1
        total /= lista_numeros[tamanho] 
    return total  


