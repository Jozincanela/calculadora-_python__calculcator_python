from funções import *


print("bem vindo a calculadora !!")

continuar = "S"
codigo = "S"
while codigo != "N": 
    while continuar != "N":    
        numero = int(input("digite um numero: "))
        lista_numeros = []
        lista_numeros.append(numero)
        continuar = input("deseja continuar colocando numeros na equação? (S/N)")
    decisao = int(input("sabendo a tabela \n 1-soma \n 2-subtração \n 3-multiplicação \n 4-divisão \n escolha: "))
    if decisao ==1 :
        print(soma(lista_numeros))    
    elif decisao ==2:
        print(subtracao(lista_numeros))
    elif decisao ==3:
        print(multiplicacao(lista_numeros))  
    elif decisao ==4:
       print(divisao(lista_numeros)) 
    
    codigo = input("deseja continuar? (S/N): ")
    
        