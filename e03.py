"""Ler um vetor Q de 20 posições (aceitar somente números positivos). 
Escrever a seguir:
o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;
"""
import random

q = []

for i in range(20):
    n = random.randrange(1, 100)
    q.append(n)

qMax = max(q)
qMin = min(q)
print(q)
print(f"O maior elemento de Q é {qMax} e está na posição {q.index(qMax)}")
print(f"O menor elemento de Q é {qMin} e está na posição {q.index(qMin)}")
