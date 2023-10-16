"""Crie um vetor N que seja resultado
 da soma dos itens de outros dois vetores A e B. 
 Exemplo: A[0] + B[0] deverá ser salva em N[0].
"""

import random


A = []
for i in range(10):
    n = random.randint(1, 50)
    A.append(n)


B = []
for i in range(10):
    n = random.randint(1, 50)
    B.append(n)


N = []
for i in range(10):
    N.append(A[i] + B[i])


print(A)
print(B)
print(N)
