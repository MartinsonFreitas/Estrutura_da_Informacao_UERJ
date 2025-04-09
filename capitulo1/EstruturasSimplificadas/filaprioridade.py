    # Fila de prioridade por tamanho de linha
    # em caso de empate, ordenar alfabeticamente
class FilaPrioridade:
    def __init__(self):
        self.elements = []
        self.counter = 0

    def add(self, element):
        priority = (len(element), self.counter, element)
        self.elements.append(priority)
        self.counter += 1
        self._sort()

    def remove(self):
        if not self.is_empty():
            _, _, element = self.elements.pop(0)
            return element
    
    def size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0

    def _sort(self):
        self.elements.sort(key=lambda x: (x[0], x[2]))

    def __contains__(self, element):
        return any(element == e[2] for e in self.elements)

    def __str__(self):
        return str([e[2] for e in self.elements])
