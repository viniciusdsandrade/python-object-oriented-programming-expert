class DoubleLinkedListCircularDisoreded:
    class Node:
        def __init__(self, elemento=None, proximo=None, anterior=None):
            self.elemento = elemento
            self.proximo = proximo
            self.anterior = anterior

        def getElemento(self):
            return self.elemento

        def getProximo(self):
            return self.proximo

        def getAnterior(self):
            return self.anterior

        def __copy__(self):
            return DoubleLinkedListCircularDisoreded.Node(self.elemento, self.proximo, self.anterior)

        def __eq__(self, other):
            if self is other: return True
            if other is None or self.__class__ != other.__class__: return False
            return self.elemento == other.elemento

        def __hash__(self):
            prime = 31
            hash_code = 1
            hash_code = prime * hash_code + (0 if self.elemento is None else hash(self.elemento))
            return abs(hash_code)

        def __str__(self):
            if self.proximo:
                return f'{self.elemento} <-> {self.proximo.elemento}'
            else:
                return str(self.elemento)

    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def getPrimeiro(self):
        return self.primeiro

    def getUltimo(self):
        return self.ultimo

    def getTamanho(self):
        return self.tamanho

    def addLast(self, elemento):
        if elemento is None:
            raise ValueError("Elemento não pode ser nulo.")

        novo = DoubleLinkedListCircularDisoreded.Node(
            elemento)  # Presumindo que a função verifyAndCopy seja implementada em Python

        if self.primeiro is None:
            self.primeiro = novo
            novo.proximo = novo  # O novo nó aponta para si mesmo
            novo.anterior = novo  # O novo nó aponta para si mesmo
            self.ultimo = novo
            self.tamanho += 1
            return

        self.ultimo.proximo = novo
        novo.anterior = self.ultimo
        novo.proximo = self.primeiro  # Torna o novo nó circular
        self.primeiro.anterior = novo  # Atualiza o anterior do primeiro nó para o novo nó
        self.ultimo = novo
        self.tamanho += 1

    def addFirst(self, elemento):
        if elemento is None:
            raise ValueError("Elemento não pode ser nulo.")

        novo = DoubleLinkedListCircularDisoreded.Node(
            elemento)

        if self.primeiro is None:
            self.primeiro = novo
            novo.proximo = novo
            novo.anterior = novo
            self.ultimo = novo
            self.tamanho += 1
            return

        novo.proximo = self.primeiro
        novo.anterior = self.ultimo
        self.primeiro.anterior = novo
        self.ultimo.proximo = novo
        self.primeiro = novo

        self.tamanho += 1

    def add(self, elemento, indice):
        if indice < 0 or indice > self.tamanho:
            raise IndexError("Índice fora dos limites da lista.")

        if indice == 0:
            self.addFirst(elemento)
            return

        if indice == self.tamanho:
            self.addLast(elemento)
            return

        novo = DoubleLinkedListCircularDisoreded.Node(elemento)
        temp = self.primeiro
        for i in range(indice):
            temp = temp.proximo

        temp.anterior.proximo = novo
        novo.anterior = temp.anterior
        novo.proximo = temp
        temp.anterior = novo

        self.tamanho += 1

    def get(self, indice):
        if indice < 0 or indice >= self.tamanho:
            raise IndexError("Índice fora dos limites da lista.")

        temp = self.primeiro
        for i in range(indice):
            temp = temp.proximo

        return temp.elemento

    def getFirst(self):
        if self.primeiro is None:
            raise ValueError("Lista vazia.")
        return self.primeiro.elemento

    def getLast(self):
        if self.ultimo is None:
            raise ValueError("Lista vazia.")
        return self.ultimo.elemento

    def remoteFirst(self):
        if self.primeiro is None:
            raise ValueError("Lista vazia.")

        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
            self.tamanho = 0
            return

        self.primeiro = self.primeiro.proximo
        self.primeiro.anterior = self.ultimo
        self.ultimo.proximo = self.primeiro

        self.tamanho -= 1

    def removeLast(self):
        if self.primeiro is None:
            raise ValueError("Lista vazia.")

        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
            self.tamanho = 0
            return

        self.ultimo.anterior.proximo = self.primeiro
        self.primeiro.anterior = self.ultimo.anterior
        self.ultimo = self.ultimo.anterior

        self.tamanho -= 1

    def remote(self, indice):
        if indice < 0 or indice >= self.tamanho:
            raise IndexError("Índice fora dos limites da lista.")

        if indice == 0:
            self.remoteFirst()
            return

        if indice == self.tamanho - 1:
            self.removeLast()
            return

        temp = self.primeiro
        for i in range(indice):
            temp = temp.proximo

        temp.anterior.proximo = temp.proximo
        temp.proximo.anterior = temp.anterior

        self.tamanho -= 1

    def isEmpty(self):
        return self.tamanho == 0

    def __len__(self):
        return self.tamanho

    def __clear__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def __index__(self, item):
        temp = self.primeiro
        for i in range(self.tamanho):
            if temp.elemento == item:
                return i
            temp = temp.proximo
        return -1

    def __contains__(self, item):
        temp = self.primeiro
        for _ in range(self.tamanho):
            if temp.elemento == item:
                return True
            temp = temp.proximo
        return False

    def __copy__(self):
        """
        Construtor que cria uma cópia da lista duplamente encadeada circular desordenada fornecida.
        """
        if self is None:
            raise ValueError("Lista não pode ser nula.")

        if self.primeiro is None:
            self.primeiro = None
            self.ultimo = None
            self.tamanho = 0
            return

        temp = self.primeiro
        while temp is not None and temp != self.ultimo:
            self.addLast(temp.elemento)  # Assumindo que add_last está implementado
            temp = temp.proximo

        if self.ultimo is not None:
            self.addLast(self.ultimo.elemento)

        self.tamanho = self.tamanho

    def __eq__(self, other) -> bool:
        if self is other: return True
        if other is None: return False
        if self.__class__ != other.__class__: return False

        if self.tamanho != other.tamanho: return False

        temp1 = self.primeiro
        temp2 = other.primeiro

        for _ in range(self.tamanho):
            if temp1 != temp2: return False
            temp1 = temp1.proximo
            temp2 = temp2.proximo

        return True

    def __hash__(self):
        prime = 31
        hash_code = 1

        temp = self.primeiro
        for _ in range(self.tamanho):
            hash_code = prime * hash_code + (0 if temp is None else hash(temp))
            temp = temp.proximo

        return abs(hash_code)

    def __str__(self):
        if self.primeiro is None:
            return "[]"

        result = ["["]
        temp = self.primeiro
        primeiro_elemento = True

        while True:
            if not primeiro_elemento:
                result.append(" <-> ")
            else:
                primeiro_elemento = False
            result.append(str(temp.elemento))
            temp = temp.proximo
            if temp == self.primeiro:
                break

        result.append("]")
        return "".join(result)


def test():
    lista = DoubleLinkedListCircularDisoreded()
    lista.addLast(1)
    lista.addLast(2)
    lista.addLast(3)
    lista.addLast(4)
    lista.addLast(5)

    print(lista)
    print(lista.getPrimeiro())
    print(lista.ultimo.proximo)
    print(lista.primeiro.anterior.anterior.anterior.anterior.anterior)

    for i in range(lista.getTamanho()):
        print("Elemento na posição", i, ":", lista.get(i))


def main():
    test()


if __name__ == "__main__":
    main()
