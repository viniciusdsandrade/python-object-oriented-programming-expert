class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        if len(self.items) < 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.items == other.items
        return False

    def __hash__(self):
        prime = 31
        hash_code = 1

        for index, item in enumerate(self.items):
            hash_code *= prime + index * hash(item)

        if hash_code < 0:
            hash_code = -hash_code

        return hash_code

    def __str__(self):
        return str(self.items)


q = Queue()
q.enqueue(1)
q.enqueue(3.2)
q.enqueue("Vinícius")

r = Queue()
r.enqueue(1)
r.enqueue(3.2)
r.enqueue("Vinícius")

dado = q.peek()
print(dado)

q.dequeue()
dado = q.peek()

print(dado)
print(q)
