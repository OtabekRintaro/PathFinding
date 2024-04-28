class Stack:
    def __init__(self):
        self._content = []

    def push(self, item):
        self._content.append(item)

    def pop(self):
        return self._content.pop(self.size() - 1)

    def top(self):
        return self._content[self.size() - 1]

    def size(self):
        return len(self._content)

    def empty(self):
        return self.size() == 0
