"""Faça um algoritmo para ler dois vetores V1 e V2 de 10 números cada. 
Calcular e escrever a quantidade de vezes que V1 e V2 
possuem os mesmos números e nas mesmas posições.
"""
V1 = [265, 904, 81, 243, 58, 37, 13, 1917, 666, 52]
V2 = [265, 28, 12, 243, 96, 37, 52, 666, 1917, 4]
comum = []

i = 0
while i < 10:
    if V1[i] == V2[i]:
        comum.append(V1[i])
    i += 1

print(f"V1 e V2 possuem os mesmos números e nas mesmas posições {len(comum)} vezes")
