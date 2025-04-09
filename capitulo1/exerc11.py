from EstruturasSimplificadas import *
from random import randint

def exerc11():
    # Suponha que você tenha uma Pilha, s, que suporta somente as operações
    # push(x) e pop(). Mostre como, usando somente uma fila FIFO, f, você
    # pode reverter a ordem de todos os elementos em s.
    
# Criando e preenchendo a pilha inicial com valores aleatórios
    s = Pilha()
    for _ in range(10):
        s.push(randint(1, 100))
        
    # Função auxiliar para visualizar a pilha
    def print_pilha(pilha):
        elementos = []
        temp = Pilha()
        # Extrai todos os elementos para uma lista temporária
        while pilha.size() > 0:
            elemento = pilha.pop()
            elementos.append(elemento)
            temp.push(elemento)
        # Reconstroi a pilha original
        while temp.size() > 0:
            pilha.push(temp.pop())
        # Imprime os elementos (do topo para a base)
        print("Pilha:", elementos[::-1])
        
    print("Pilha original:")
    print_pilha(s)  # Assumindo que a classe Pilha tem um método __str__ implementado
    
    # Fila auxiliar que será usada para reverter a pilha
    f = Fila()
    
    # Passo 1: Transferir todos os elementos da pilha para a fila
    while s.size() > 0:
        f.add(s.pop())
    
    # Passo 2: Transferir os elementos de volta para a pilha
    while f.size() > 0:
        s.push(f.remove())
    
    print("\nPilha após reversão:")
    print_pilha(s)

   
if __name__ == "__main__":
    exerc11()
