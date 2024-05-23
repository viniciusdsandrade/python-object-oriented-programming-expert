class No:
    def __init__(self, info=None, esq=None, dir=None):
        self._info = info
        self._esq = esq
        self._dir = dir

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, valor):
        self._info = valor

    @property
    def esq(self):
        return self._esq

    @esq.setter
    def esq(self, esquerda):
        self._esq = esquerda

    @property
    def dir(self):
        return self._dir

    @dir.setter
    def dir(self, direita):
        self._dir = direita

    def buscar_no(self, valor):
        if valor is None:
            return None

        if valor == self.info:
            return self
        elif valor < self.info and self.esq is not None:
            return self.esq.buscar_no(valor)
        elif valor > self.info and self.dir is not None:
            return self.dir.buscar_no(valor)
        else:
            return None

    def buscar_minimo(self):
        if self.esq is None:
            return self.info
        else:
            return self.esq.buscar_minimo()

    def buscar_maximo(self):
        if self.dir is None:
            return self.info
        else:
            return self.dir.buscar_maximo()

    def is_folha(self):
        return self.esq is None and self.dir is None

    def tem_ambos_filhos(self):
        return self.esq is not None and self.dir is not None

    def tem_um_filho(self):
        return (self.esq is not None and self.dir is None) or (self.esq is None and self.dir is not None)

    def __str__(self, nivel=0):
        sb = ""
        sb += "  " * nivel  # Indentação para representar a hierarquia

        sb += "|- "
        sb += str(self.info)
        sb += "\n"

        if self.esq is not None:
            sb += self.esq.__str__(nivel + 1)
        else:
            sb += self.gerar_string_filho_nulo(nivel + 1, "Esq")

        if self.dir is not None:
            sb += self.dir.__str__(nivel + 1)
        else:
            sb += self.gerar_string_filho_nulo(nivel + 1, "Dir")

        return sb

    @staticmethod
    def gerar_string_filho_nulo(nivel, tipo):
        sb = ""
        sb += "  " * nivel
        sb += "|- "
        sb += tipo
        sb += ": Nulo\n"
        return sb


if __name__ == "__main__":
    # Teste 1: Criar um nó e verificar seu valor
    no1 = No(10)
    print("Valor do nó 1:", no1.info)  # Saída: 10

    # Teste 2: Modificar o valor do nó e verificar
    no1.info = 20
    print("Valor do nó 1 após modificação:", no1.info)  # Saída: 20

    # Teste 3: Criar nós filhos e verificar a estrutura da árvore
    no1.esq = No(5)
    no1.dir = No(15)
    print("Árvore:")
    print(no1)  # Saída: A representação da árvore, mostrando os nós filhos

    # Teste 4: Buscar um valor na árvore
    no_encontrado = no1.buscar_no(15)
    if no_encontrado:
        print("Nó encontrado com valor:", no_encontrado.info)
    else:
        print("Nó não encontrado.")
