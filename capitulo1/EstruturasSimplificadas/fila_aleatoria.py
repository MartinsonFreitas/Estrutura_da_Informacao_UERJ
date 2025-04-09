from .fila import Fila
from random import randrange

class FilaAleatoria(Fila):
    # escreva o método remove que remove um elemento aleatório da fila
    # fique atento, pois se você remover diretamente um elemento aleatório
    # sua implementação será O(n), onde n é o tamanho da fila.
    # Você deve implementar este método de forma que ele seja O(1).
    
    # Para isso, você deve usar o método pop da lista, que remove o último
    # elemento da lista e retorna o elemento removido.
    # Para remover um elemento aleatório, você deve:
    # 1. gerar um índice aleatório entre 0 e o tamanho da fila - 1
    # 2. guardar o elemento que está no índice aleatório
    # 3. guardar o último elemento da fila
    # 4. remover o último elemento da fila
    # 5. colocar o último elemento no índice aleatório
    # 6. remover o elemento guardado no índice aleatório
    # 7. retornar o elemento guardado no índice aleatório
    # 8. O método deve ser O(1)
    # 9. O método deve lançar uma exceção IndexError se a fila estiver vazia
    # 10. O método deve ser chamado remove, e não pop
    # 11. O método deve receber um parâmetro opcional i, que é o índice do elemento
    # que será removido. Se o parâmetro i for passado, o método deve remover
    # o elemento no índice i, e não um elemento aleatório.
    # 12. O método deve ser chamado remove, e não pop
    # 13. O método deve ser O(1) mesmo se o parâmetro i for passado.
     
     # construtor
    # chama o construtor da classe pai
    # e inicializa o dicionário index_map
    # que irá mapear os elementos da fila para seus índices
    # na fila
    # CUIDADO: não use self.fila = [] aqui, pois isso irá
    # apagar a fila da classe pai.
    # O correto é usar self.fila.append(item) para adicionar
    # elementos à fila.
    def __init__(self): 
        super().__init__()        
        self.index_map = {}
        
    def add(self, item):
        if item not in self.index_map:
            self.index_map[item] = len(self.fila)
            self.fila.append(item)
    
    def remove(self, i = 0):
        #pass # apague esta linha
        # e escreva sua resposta
        # CUIDADO: o pass da linha acima faz o programa de teste entrar 
        # em loop infinito. Por quê?
        
        if not self:
            raise IndexError("A fila está vazia")
        
        random_index = randrange(len(self.fila))
        removed_item = self.fila[random_index]
        last_item = self.fila.pop()
        
        if random_index < len(self.fila):
            self.fila[random_index] = last_item
            self.index_map[last_item] = random_index
        
        del self.index_map[removed_item]
        
        return removed_item
        
