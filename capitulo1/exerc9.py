from EstruturasSimplificadas import *
from random import randint

def exerc9(nome_arq = 'in9.txt'):
    # Ler a entrada completa, uma linha por vez, e imprimi-las em uma ordem aleatória.

    # Você deve modificar o arquivo fila_aleatoria.py do modulo EstruturasSimplificadas
    # para implementar a estrutura de dados
    # FilaAleatoria. Esta estrutura deve ser uma fila que remove um elemento aleatório

    # criar uma fila vazia
    fila = FilaAleatoria()

    arq = open(nome_arq, "r")
    # ler cada linha do arquivo de entrada e inserir no conjunto
    for linha in arq:
        fila.add(linha.strip())

    # imprimir cada linha
    while fila.size() > 0:
        print(fila.remove())

    # fechar arquivo de entrada
    arq.close()

if __name__ == "__main__":
    exerc9()