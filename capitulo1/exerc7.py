from EstruturasSimplificadas import *

def exerc7():
    # Ler uma linha por vez. Então imprimir todas as linhas ordenadas por
    # tamanho, com a linha mais curta em primeiro. No caso em que duas linhas
    # tenham o mesmo tamanho, resolva sua ordem usando a regra de ordenação alfabética. 
    # as linhas duplicadas devem ser impressas o mesmo número de vezes 
    # que aparecem na entrada.
    
    try:
        arq = open("in7.txt", "r")
    except:
        print("Erro ao abrir arquivo de entrada.")
        return

    # Linhas
    linhas = FilaPrioridade()
    
    # Ler uma linha por vez e adicionar a linha ao conjunto de linhas
    for linha in arq:
        # Remove espaços em branco no início e no fim da linha
        linha = linha.strip()
        
        # Adicionar a linha ao conjunto de linhas
        linhas.add(linha)
        
    while linhas.size() > 0:
        print(linhas.remove())
        
    # fechar arquivo de entrada
    arq.close()

if __name__ == "__main__":
    exerc7()
