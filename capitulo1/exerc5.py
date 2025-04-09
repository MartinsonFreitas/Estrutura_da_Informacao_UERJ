from EstruturasSimplificadas import *

def exerc5(nome_arq = "in5.txt"):
    # Ler uma linha por vez e imprimir uma linha somente se você já tiver lido
    # esta linha anteriormente. O resultado final é que você remove a primeira
    # ocorrência de cada linha. Preste atenção para que um arquivo com muitas
    # linhas duplicadas não utilize mais memória que aquela necessária para o
    # número de linhas únicas.

    try:
        arq = open(nome_arq, "r")
    except:
        print("Erro ao abrir arquivo de entrada.")
        return
    
    # Escreva aqui sua resposta para o exercício 5. Não esqueça de usar a função strip()
    # para remover os espaços em branco no início e no fim da string.
    # ATENÇÃO: não use a função readlines() para ler o arquivo de entrada.
    # Sua saída deve ser escrita usando a função print().
    # Você deve usar a estrutura simplificada Pilha, Fila, Deque, SSet, USet ou FilaPrioridade
   
    linhas_vistas = USet()

    for linha in arq:
        linha = linha.strip()  
        
        # Verifica se a linha já foi vista
        if linha not in linhas_vistas:
            # Adiciona a linha ao conjunto de linhas vistas
            linhas_vistas.add(linha)
       
        # Verifica se a linha já foi vista
        # Se a linha não estiver no conjunto, adiciona-a
        # ao conjunto de linhas vistas
        # e imprime a linha
        elif linhas_vistas.find(linha) is not None:
            print(linha)
        else:
            linhas_vistas.add(linha)
   
    # Fim da sua resposta para o exercício 5.
    # fechar arquivo de entrada
    arq.close()

if __name__ == "__main__":
    exerc5()
