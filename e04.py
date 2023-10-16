"""Ler um vetor A de 10 números. 
Após, ler mais um número e guardar em uma variável X. 
Armazenar em um vetor M o resultado de cada elemento de A 
multiplicado pelo valor X. 
Logo após, imprimir o vetor M.
"""
import random

A = []

for i in range(10):
    n = random.randint(1, 50)
    A.append(n)

X = random.randint(1, 10)
print(A, X)
M = []

for j in A:
    multi = j * X
    M.append(multi)

print(M)
