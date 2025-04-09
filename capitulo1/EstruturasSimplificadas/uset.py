
class USet:
    #class que implementa um conjunto não ordenado de elementos simples
    def __init__(self):
        self.conjunto = []

    # add(x): acrescenta o elemento x ao conjunto se ele ainda não estiver presente. 
    # Acrescenta x ao conjunto desde que não exista nenhum elemento y
    # no conjunto de tal modo que x seja igual a y. Retorna true se x foi
    # acrescentado ao conjunto e false caso contrário.
    def add(self, x):
        if x not in self.conjunto:
            self.conjunto.append(x)
            return True
        return False

    # remove(x): remove x do conjunto;
    # Encontra um elemento y no conjunto de modo que x seja igual a y e
    # remove y. Retorna y, ou None se tal elemento não existe.
    def remove(self, x):
        if x in self.conjunto:
            self.conjunto.remove(x)
            return x
        return None

    # find(x): encontra x no conjunto se ele existe;
    # Encontra um elemento y no conjunto de modo que y seja igual a x.
    # Retorna y, ou None se tal elemento não existe.
    def find(self, x):
        if x in self.conjunto:
            return x
        return None

    # size(): retorna o número, n, de elementos no conjunto;
    def size(self):
        return len(self.conjunto)
    
    def __iter__(self):
        return iter(self.conjunto)
     