"""Escreva um algoritmo que permita a 
leitura das notas de uma turma de 20 alunos.
 Calcular a média da turma e 
 contar quantos alunos obtiveram nota acima desta média calculada. 
 Escrever a média da turma e o resultado da contagem.
"""
import random
from statistics import mean

notas_turma = []

for i in range(20):
    # para eu não ter que criar as 20 notas dos alunos
    notas_individuais = random.randrange(0, 10)
    notas_turma.append(notas_individuais)

media = mean(notas_turma)


def acima_da_media(notas, media):
    acima = []
    for i in notas:
        if i >= media:
            acima.append(i)
        else:
            pass

    return len(acima)


print(notas_turma)
print(
    f"A média da turma foi {media} e {acima_da_media(notas_turma, media)} alunos tiveram notas acima dessa média"
)
