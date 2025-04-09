class Pilha:
    def __init__(self):
        self.pilha = []
    def push(self, valor):
        self.pilha.append(valor)

    def pop(self):
        if not self.pilha:
            raise IndexError("A pilha está vazia")
        return self.pilha.pop()
    
    def size(self):
        return len(self.pilha)