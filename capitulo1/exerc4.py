from EstruturasSimplificadas import *

def exerc4(nome_arq = "in4.txt"):
    # Ler a entrada linha por linha e imprimir a linha se ela não é a
    # duplicata de alguma linha anterior. Preste atenção para que um
    # arquivo com muitas linhas duplicadas não utilize mais memória que
    # aquela necessária para o número de linhas únicas.
    # Por exemplo, se o arquivo de entrada contém 1000 linhas, mas cada uma
    # delas é uma cópia igual às outras, seu programa deve imprimir apenas 1 linha.

    try:
        arq = open(nome_arq, "r")
    except:
        print("Erro ao abrir arquivo de entrada.")
        return
    # Escreva aqui sua resposta para o exercício 4. Não esqueça de usar a função strip()
    # para remover os espaços em branco no início e no fim da string.
    # ATENÇÃO: não use a função readlines() para ler o arquivo de entrada.
    # Sua saída deve ser escrita usando a função print().
    # Você deve usar a estrutura simplificada Pilha, Fila, Deque, SSet, USet ou FilaPrioridade

    linhas_unicas = SSet()

    # Varre o arquivo linha por linha
    for linha in arq:
        linha = linha.strip()
        #print(linha)
        if linha not in linhas_unicas:
            print(linha)
            # Adiciona a linha ao conjunto de linhas únicas
            linhas_unicas.add(linha)

    # Fim da sua resposta para o exercício 4.
    # fechar arquivo de entrada
    arq.close()

if __name__ == "__main__":
    exerc4()
