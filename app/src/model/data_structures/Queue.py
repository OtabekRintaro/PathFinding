class Queue:
    content = []

    def push(self, item):
        self.content.append(item)

    def pop(self):
        return self.content.pop(0)

    def front(self):
        return self.content[0]

    def size(self):
        return len(self.content)

    def empty(self):
        return self.size() == 0
