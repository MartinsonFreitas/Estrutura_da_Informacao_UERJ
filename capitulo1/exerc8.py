from EstruturasSimplificadas import *

def exerc8(nome_arq = "in8.txt"):
    # Leia toda a entrada uma linha de cada vez e, em seguida, imprimir
    # as linhas pares (começando com a primeira linha, linha 0) seguida pelas linhas ímpares.

    try:
        arq = open(nome_arq, "r")
    except:
        print("Erro ao abrir arquivo de entrada.")
        return
    
    # Escreva aqui sua resposta para o exercício 8. Não esqueça de usar a função strip()
    # para remover os espaços em branco no início e no fim da string.
    # ATENÇÃO: não use a função readlines() para ler o arquivo de entrada.
    # Sua saída deve ser escrita usando a função print().
    # Você deve usar a estrutura simplificada Pilha, Fila, Deque, SSet, USet ou FilaPrioridade

    impares = Deque()  # Mais eficiente que Fila para alguns casos
    linha_atual = 0

    for linha in arq:
        linha = linha.strip()
        if linha_atual % 2 == 0:
            print(linha)
        else:
            impares.add_last(linha)  # Adiciona no final
        linha_atual += 1

    while impares.size() > 0:
        print(impares.remove_first())  # Remove do início

    # fechar arquivo de entrada
    arq.close()

if __name__ == "__main__":
    exerc8()
