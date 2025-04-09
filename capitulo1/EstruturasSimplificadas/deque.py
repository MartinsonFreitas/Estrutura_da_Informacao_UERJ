class Deque:
    def __init__(self):
        self.items = []

    def add_first(self, item):
        self.items.append(item)

    def add_last(self, item):
        self.items.insert(0,item)

    def remove_first(self):
        return self.items.pop()

    def remove_last(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)