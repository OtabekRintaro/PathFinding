class Queue:

    def __init__(self):
        self._content = []

    def push(self, item):
        self._content.append(item)

    def pop(self):
        return self._content.pop(0)

    def front(self):
        return self._content[0]

    def size(self):
        return len(self._content)

    def empty(self):
        return self.size() == 0
