class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 0:
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) < 0:
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def __eq__(self, other):
        if isinstance(other, Stack):
            return self.stack == other.stack
        return False

    def __hash__(self):
        prime = 31
        hash_code = 1

        for index, item in enumerate(self.stack):
            hash_code *= prime + index * hash(item)

        if hash_code < 0:
            hash_code = -hash_code

        return hash_code

    def __str__(self):
        return str(self.stack)


s = Stack()
s.push(1)
s.push(3.2)
s.push("Vinícius")

r = Stack()
r.push(1)
r.push(3.2)
r.push("Vinícius")

dado = s.peek()
print(dado)

s.pop()
dado = s.peek()
print(dado)

hash_1 = hash(s)
hash_2 = hash(r)

print(hash_1)
print(hash_2)

s_is_equal_t = s.__eq__(r)

print(s)
print(r)
print(s_is_equal_t)
