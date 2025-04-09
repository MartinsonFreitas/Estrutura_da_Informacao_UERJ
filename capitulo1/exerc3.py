from EstruturasSimplificadas import *

def exerc3(nome_arq = "in3.txt"):
# Ler a entrada uma linha por vez. Em qualquer momento, após ter lido
# as primeiras 42 linhas, se alguma linha é vazia (isto é, uma string de tamanho zero), 
# então imprima a linha que ocorreu 42 linhas antes dela.
# Por exemplo, se a linha 242 é vazia, seu programa deve imprimir a linha
# 200. Seu programa deve ser implementado de tal maneira que ele nunca
# armazene mais de 43 linhas da entrada, em qualquer momento.

    try:
        arq = open(nome_arq, "r")
    except IOError:
        print("Erro ao abrir arquivo de entrada.")
        return
    # Escreva aqui sua resposta para o exercício 3. Não esqueça de usar a função strip()
    # para remover os espaços em branco no início e no fim da string.
    # ATENÇÃO: não use a função readlines() para ler o arquivo de entrada.
    # Sua saída deve ser escrita usando a função print().
    # IMPORTANTE: Seu código nunca deverá ter armazenado mais de 43 linhas.
    # Você deve usar a estrutura simplificada Pilha, Fila, Deque, Sset, Uset ou FilaPrioridade

    fila = Fila()
    n = 0
    
    # Lê cada linha do arquivo e adiciona à fila
    for linha in arq:           
        fila.add(linha.strip())
        
        #print(f'Adicionando a linha {n} na fila')   
        if linha.strip() == "" and fila.size() > 42:
            #print(f'A linha {n}  está vazia')                
            print(fila.remove())
            
        elif fila.size() == 43:
            fila.remove()
            #fila.add(linha.strip())
        
        n += 1      

    # Fim da sua resposta para o exercício 3.
    # fechar arquivo de entrada
    arq.close()

if __name__ == "__main__":
    exerc3()
