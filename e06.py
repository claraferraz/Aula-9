"""Faça um algoritmo para ler um vetor de 20 números.
 Após isto, deverá ser lido mais um número qualquer e 
 verificar se esse número existe no vetor ou não.
Se existir, o algoritmo deve gerar um novo vetor sem esse número. 
(Considere que não haverão números repetidos no vetor).
"""
if __name__ == "__main__":
    n = int(input("digite um número: "))

vetor = [71, 12, 33, 80, 72, 52, 41, 74, 31, 49, 40, 2, 61, 81, 43, 79, 45, 84, 42, 56]


def tentativa(n):
    try:
        posicao = vetor.index(n)
        return vetor.pop(posicao)
    except ValueError:
        return "o número digitado não encontra-se no vetor"


if __name__ == "__main__":
    print(tentativa(n))
