class LinkedListDisordered:
    class Node:
        def __init__(self, valor, next_node=None):
            self.data = valor
            self.next = next_node

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def __hash__(self):
            prime = 31
            hash_code = 1

            hash_code *= prime + (hash(self.data) if self.data is not None else 0)

            if hash_code < 0:
                hash_code = -hash_code

            return hash_code

        def __eq__(self, obj):
            if self is obj: return True
            if obj is None: return False
            if not isinstance(obj, LinkedListDisordered.Node): return False
            return self.data == obj.data

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.head = None
        self.size = 0

    def add_last(self, item):
        novo = self.Node(item)

        if self.head is None:
            self.head = novo
        else:
            atual = self.head
            while atual.next is not None:
                atual = atual.next
            atual.next = novo
        self.size += 1

    def add_first(self, item):
        novo = self.Node(item)
        novo.next = self.head
        self.head = novo
        self.size += 1

    def add_at(self, valor, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.add_first(valor)
            return

        if index == self.size:
            self.add_last(valor)
            return

        novo = self.Node(valor)
        aux = self.head

        for i in range(index - 1):
            aux = aux.next

        novo.next = aux.next
        aux.next = novo
        self.size += 1

    def remove_first(self):
        if self.head is None:
            raise IndexError("Empty list")

        self.head = self.head.next
        self.size -= 1

    def remove_last(self):
        if self.head is None:
            raise IndexError("Empty list")

        if self.head.next is None:
            self.head = None
            self.size -= 1
            return

        atual = self.head
        while atual.next.next is not None:
            atual = atual.next

        atual.next = None
        self.size -= 1

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.remove_first()
            return

        if index == self.size - 1:
            self.remove_last()
            return

        aux = self.head
        for i in range(index - 1):
            aux = aux.next

        aux.next = aux.next.next
        self.size -= 1

    def __contains__(self, item):
        atual = self.head
        while atual is not None:
            if atual.value == item:
                return True
            atual = atual.next
        return False

    def is_empty(self):
        return self.size == 0

    def get_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        atual = self.head
        for i in range(index):
            atual = atual.next

        return atual.value

    def get_last(self):
        if self.head is None:
            raise IndexError("Empty list")

        atual = self.head
        while atual.next is not None:
            atual = atual.next

        return atual.value

    def get_first(self):
        if self.head is None:
            raise IndexError("Empty list")
        return self.head.value

    def __reversed__(self):
        atual = self.head
        anterior = None
        while atual is not None:
            proximo = atual.next
            atual.next = anterior
            anterior = atual
            atual = proximo
        self.head = anterior

    def rotate(self, passos):
        if self.head is None or self.head.next is None:
            return

        passos = passos % self.size

        if passos < 0:
            passos = self.size + passos

        if passos == 0:
            return

        aux = self.head
        for i in range(self.size - passos - 1):
            aux = aux.next

        novo_head = aux.next
        aux.next = None

        aux = novo_head
        while aux.next:
            aux = aux.next

        aux.next = self.head
        self.head = novo_head

    def sort(self, comparator=None):
        if self.head is None or self.head.next is None:
            return

        if comparator is None:
            self._sort_default()
        else:
            self._sort_custom(comparator)

    def _sort_default(self):
        atual = self.head

        while atual:
            indice = atual.next

            while indice:
                if atual.data > indice.data:
                    temp = atual.data
                    atual.data = indice.data
                    indice.data = temp
                indice = indice.next
            atual = atual.next

    def _sort_custom(self, comparator):
        atual = self.head

        while atual:
            indice = atual.next

            while indice:
                if comparator(atual.data, indice.data) > 0:
                    temp = atual.data
                    atual.data = indice.data
                    indice.data = temp
                indice = indice.next
            atual = atual.next

    def shuffle(self):
        import random

        if self.head is None or self.head.next is None:
            return

        atual = self.head

        while atual:
            indice = atual.next

            while indice:
                indice_aleatorio = random.randint(0, 1)
                if indice_aleatorio == 0:
                    temp = atual.data
                    atual.data = indice.data
                    indice.data = temp
                indice = indice.next
            atual = atual.next

    def __hash__(self):
        prime = 31
        hash_code = 1
        aux = self.head

        while aux:
            hash_code *= prime + (aux.data.__hash__() if aux.data is not None else 0)
            aux = aux.next

        if hash_code < 0:
            hash_code = -hash_code

        return hash_code

    def __eq__(self, other):
        if self is other: return True
        if not isinstance(other, LinkedListDisordered): return False
        if self.size != other.size: return False

        this_node = self.head
        other_node = other.head

        while this_node and other_node:
            if this_node.data != other_node.data:
                return False
            this_node = this_node.next
            other_node = other_node.next

        return this_node is None and other_node is None

    def __len__(self):
        return self.size

    def __str__(self):
        result = "["
        aux = self.head
        while aux:
            result += str(aux.data)
            if aux.next:
                result += " -> "
            aux = aux.next
        result += "]"
        return result


if __name__ == "__main__":
    lista = LinkedListDisordered()
    lista.add_first(1)
    lista.add_first(2)
    lista.add_first(3)
    lista.add_first(4)
    lista.add_first(5)
    lista.add_first(6)
    lista.add_first(7)
    lista.add_first(8)
    lista.add_first(9)
    lista.add_first(10)

    lista_2 = LinkedListDisordered()
    lista_2.add_last(1)
    lista_2.add_last(2)
    lista_2.add_last(3)
    lista_2.add_last(4)
    lista_2.add_last(5)
    lista_2.add_last(6)
    lista_2.add_last(7)
    lista_2.add_last(8)
    lista_2.add_last(9)
    lista_2.add_last(10)

    print("Lista 1")
    print(lista)

    print("Lista 2")
    print(lista_2)

    print("Rotacionando 3 passos lista 1")
    lista.rotate(3)
    print(lista)

    print("Rotacionando 3 passos lista 2")
    lista_2.rotate(3)
    print(lista_2)

    print("Rotacionando -3 passos lista 1")
    lista.rotate(-3)
    print(lista)

    print("Rotacionando -3 passos lista 2")
    lista_2.rotate(-3)
    print(lista_2)

    print("Ordenando a lista 1")
    lista.sort()
    print(lista)

    print("reverse a lista 2")
    lista_2.__reversed__()
    print(lista_2)

    print("Embaralhando a lista")
    lista.shuffle()
    print(lista)

    lista.sort(lambda x, y: y - x)
    print(lista)
