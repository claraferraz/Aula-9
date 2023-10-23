"""Ler uma matriz D 5 x 5 (considere que não serão informados valores duplicados). 
A seguir, leia um número X e escreva uma mensagem 
indicando se o valor de X existe ou NÃO na matriz.
"""
matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [1, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
x = int(input("digite um número: "))


def palpite(matriz, x):
    # o enumerate retorna o índice e o valor daquele índice na array
    for indice, lista in enumerate(matriz):
        try:
            lista.index(x)
            return "Existe na matriz"
        except ValueError:
            if indice == 4:
                return "Não existe na matriz"
            else:
                pass


print(palpite(matriz, x))
