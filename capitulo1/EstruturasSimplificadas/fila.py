class Fila:
# Classe Fila simplificada
    def __init__(self):
        self.fila = []
        
    def add(self, elemento):
        self.fila.append(elemento)

    def remove(self, i = 0):
        return self.fila.pop(i)
    
    def size(self):
        return len(self.fila)
    
    def imprimir(self):
        print(self.fila)