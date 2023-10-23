"""Faça um algoritmo para ler um vetor de 30 números. 
Após isto, ler mais um número qualquer, 
calcular e escrever quantas vezes esse número aparece no vetor.
"""
import random


def vetor():
    v = []
    for i in range(30):
        v.append(random.randint(0, 100))
    return v


lista = vetor()
print(lista)

n = int(input("Digite um número de 0 a 100: "))


def contador(lista, n):
    repete = lista.count(n)
    if repete == 0:
        return f"{n} não existe no vetor"
    else:
        return f"{n} se repete {repete} vezes no vetor"


print(contador(lista, n))
