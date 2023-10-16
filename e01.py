"""Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol 
e armazene os nomes lidos em um vetor (lista). 
Após isto, o algoritmo deve permitir a leitura de mais 
1 nome qualquer de clube e 
depois escrever a mensagem ACHEI, 
se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), 
ou NÃO ACHEI caso contrário."""


if __name__ == "__main__":
    procura = input("Qual time você quer achar? ")


def tentativa(procura):
    clubes = [
        "botafogo",
        "vasco",
        "fluminense",
        "botafogo da PB",
        "palmeiras",
        "atlético mineiro",
        "grêmio",
        "bahia",
        "flamengo",
        "chapecoense",
    ]
    try:
        clubes.index(procura)
        return "ACHEI"
    except ValueError:
        return "NÃO ACHEI"


if __name__ == "__main__":
    print(tentativa(procura))
