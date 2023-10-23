"""
DESAFIO | Construa uma matriz 10 x 10 com valores randômicos. 
A matriz não pode ter valores repetidos. 
Depois apresente:
o resultado da soma de todos os valores da matriz;
o resultado da soma dos valores da diagonal principal;
o resultado da soma dos valores da diagonal secundária;
o resultado da soma da coluna central;
"""
import random


def cria_array():
    lista = []
    indice = 0
    while indice < 100:
        n = random.randint(100, 300)
        if lista.count(n) > 0:
            pass
        else:
            lista.append(n)
            indice += 1
    return lista


def monta_matriz(lista):
    m = []
    for i in range(0, len(lista) - 1, 10):
        indice_matriz = lista[i : i + 10]
        m.append(indice_matriz)
    return m


# Por ser uma matriz com número par de colunas, portanto, sem uma coluna central bem definida,
# defini a coluna usada para o desafio a referente aos índices 5 de cada array na matriz


def soma_coluna(matriz):
    coluna = []
    for i in range(10):
        coluna.append(matriz[i][5])
    soma = sum(coluna)
    print(coluna)
    return f"A soma dos valores da coluna principal é {soma}"


def soma_diagonal(matriz):
    diagonal1 = []
    diagonal2 = []
    j = 1
    for i in range(10):
        diagonal1.append(matriz[i][i])
        diagonal2.append(matriz[i][-j])
        j += 1
    soma_d1 = sum(diagonal1)
    soma_d2 = sum(diagonal2)
    print(diagonal1)
    print(diagonal2)
    return (
        f"A soma da diagonal principal é {soma_d1} e da diagonal secundária é {soma_d2}"
    )


lista = cria_array()
matriz = monta_matriz(lista)

for linha in matriz:
    print(linha)

soma = sum(lista)
print(f"A soma dos valores dessa matriz é {soma}")
print(soma_coluna(matriz))
print(soma_diagonal(matriz))
