from No import No


class ArvoreBinaria:
    def __init__(self, raiz=None):
        """
        Construtor da classe ArvoreBinaria.

        Args:
            raiz: O nó raiz da árvore.
        """
        if raiz is not None and not isinstance(raiz, No):
            raise TypeError("A raiz deve ser um objeto do tipo 'No'")

        self._raiz = raiz

    @property
    def raiz(self):
        """Retorna o nó raiz da árvore."""
        return self._raiz

    @raiz.setter
    def raiz(self, nova_raiz):
        """Define um novo nó como raiz da árvore."""
        if nova_raiz is not None and not isinstance(nova_raiz, No):
            raise TypeError("A raiz deve ser um objeto do tipo 'No'")
        self._raiz = nova_raiz

    def inserir(self, valor):
        """
        Insere um novo valor na árvore.

        Args:
            valor: O valor a ser inserido.
        """
        if valor is None:
            raise ValueError("Valor nulo não é permitido.")

        if self._raiz is None:
            self._raiz = No(valor)
        else:
            self._inserir_recursivo(self._raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        """Método recursivo para inserir um valor na árvore."""
        if valor < no_atual.info:
            if no_atual.esq is None:
                no_atual.esq = No(valor)
            else:
                self._inserir_recursivo(no_atual.esq, valor)
        else:  # valor >= no_atual.info
            if no_atual.dir is None:
                no_atual.dir = No(valor)
            else:
                self._inserir_recursivo(no_atual.dir, valor)

    def remova(self, valor):
        """
        Remove um valor da árvore.

        Args:
            valor: O valor a ser removido.

        Raises:
            ValueError: Se o valor não for encontrado.
        """
        self._raiz = self._remova_recursivo(self._raiz, valor)

    def _remova_recursivo(self, no_atual, valor):
        """Método recursivo para remover um valor da árvore."""
        if no_atual is None:
            raise ValueError("Valor não encontrado na árvore.")

        if valor < no_atual.info:
            no_atual.esq = self._remova_recursivo(no_atual.esq, valor)
        elif valor > no_atual.info:
            no_atual.dir = self._remova_recursivo(no_atual.dir, valor)
        else:  # valor encontrado
            # Caso 1: Nó folha ou com apenas um filho
            if no_atual.esq is None:
                return no_atual.dir
            elif no_atual.dir is None:
                return no_atual.esq
            # Caso 2: Nó com dois filhos
            else:
                sucessor = self._encontre_minimo(no_atual.dir)
                no_atual.info = sucessor.info
                no_atual.dir = self._remova_recursivo(no_atual.dir, sucessor.info)
        return no_atual

    @staticmethod
    def _encontre_minimo(no_atual):
        """Encontra o nó com o menor valor na subárvore."""
        while no_atual.esq is not None:
            no_atual = no_atual.esq
        return no_atual

    def contem(self, valor):
        return self._contem_recursivo(self._raiz, valor)

    def _contem_recursivo(self, no_atual, valor):
        if no_atual is None:
            return False
        if valor == no_atual.info:
            return True
        elif valor < no_atual.info:
            return self._contem_recursivo(no_atual.esq, valor)
        else:  # valor > no_atual.info
            return self._contem_recursivo(no_atual.dir, valor)

    def get_menor(self):
        if self._raiz is None:
            raise ValueError("A árvore está vazia.")
        return self._buscar_minimo(self._raiz).info

    @staticmethod
    def _buscar_minimo(no_atual):
        while no_atual.esq is not None:
            no_atual = no_atual.esq
        return no_atual

    def get_maior(self):
        if self._raiz is None:
            raise ValueError("A árvore está vazia.")
        return self._buscar_maximo(self._raiz).info

    @staticmethod
    def _buscar_maximo(no_atual):
        while no_atual.dir is not None:
            no_atual = no_atual.dir
        return no_atual

    def esta_balanceada(self):
        return self._esta_balanceada_recursivo(self._raiz)

    def _esta_balanceada_recursivo(self, no_atual):
        if no_atual is None:
            return True
        altura_esquerda = self._altura(no_atual.esq)
        altura_direita = self._altura(no_atual.dir)
        return abs(altura_esquerda - altura_direita) <= 1 and \
            self._esta_balanceada_recursivo(no_atual.esq) and \
            self._esta_balanceada_recursivo(no_atual.dir)

    @staticmethod
    def rotacao_esquerda(no):
        nova_raiz = no.dir
        no.dir = nova_raiz.esq
        nova_raiz.esq = no
        return nova_raiz

    @staticmethod
    def rotacao_direita(no):
        nova_raiz = no.esq
        no.esq = nova_raiz.dir
        nova_raiz.dir = no
        return nova_raiz

    def balancear(self):
        self._raiz = self._balancear_recursivo(self._raiz)

    def _balancear_recursivo(self, no):
        if no is None:
            return None

        no.esq = self._balancear_recursivo(no.esq)
        no.dir = self._balancear_recursivo(no.dir)

        fator_balanceamento = self._altura(no.esq) - self._altura(no.dir)

        if fator_balanceamento > 1:
            if self._altura(no.esq.dir) > self._altura(no.esq.esq):
                no.esq = self.rotacao_esquerda(no.esq)
            no = self.rotacao_direita(no)
        elif fator_balanceamento < -1:
            if self._altura(no.dir.esq) > self._altura(no.dir.dir):
                no.dir = self.rotacao_direita(no.dir)
            no = self.rotacao_esquerda(no)
        return no

    def to_linked_list(self):
        lista = []
        self._to_linked_list_recursivo(self._raiz, lista)
        return lista

    def _to_linked_list_recursivo(self, no_atual, lista):
        if no_atual is not None:
            self._to_linked_list_recursivo(no_atual.esq, lista)
            lista.append(no_atual.info)
            self._to_linked_list_recursivo(no_atual.dir, lista)

    def espelhar(self):
        self._espelhar_recursivo(self._raiz)

    def _espelhar_recursivo(self, no_atual):
        if no_atual is not None:
            no_atual.esq, no_atual.dir = no_atual.dir, no_atual.esq
            self._espelhar_recursivo(no_atual.esq)
            self._espelhar_recursivo(no_atual.dir)

    def achar(self, valor):
        return self._achar_recursivo(self._raiz, valor)

    def _achar_recursivo(self, no_atual, valor):
        if no_atual is None or no_atual.info == valor:
            return no_atual
        if valor < no_atual.info:
            return self._achar_recursivo(no_atual.esq, valor)
        return self._achar_recursivo(no_atual.dir, valor)

    def altura(self):
        return self._altura(self._raiz)

    def _altura(self, no_atual):
        if no_atual is None:
            return -1
        return 1 + max(self._altura(no_atual.esq), self._altura(no_atual.dir))

    def profundidade(self, no):
        return self._profundidade_recursiva(self._raiz, no, 0)

    def _profundidade_recursiva(self, no_atual, no_alvo, profundidade_atual):
        if no_atual is None:
            return -1

        if no_atual.info == no_alvo.info:
            return profundidade_atual

        profundidade_esquerda = self._profundidade_recursiva(no_atual.esq, no_alvo, profundidade_atual + 1)
        if profundidade_esquerda != -1:
            return profundidade_esquerda

        return self._profundidade_recursiva(no_atual.dir, no_alvo, profundidade_atual + 1)

    def esta_vazio(self):
        return self._raiz is None

    def limpar(self):
        self._raiz = None

    def tamanho(self):
        return self._tamanho_recursivo(self._raiz)

    def _tamanho_recursivo(self, no_atual):
        if no_atual is None:
            return 0
        return 1 + self._tamanho_recursivo(no_atual.esq) + self._tamanho_recursivo(no_atual.dir)

    def __str__(self):
        if self._raiz is None:
            return "{}"
        return self._string_recursivo(self._raiz, 0, "", True)

    def _string_recursivo(self, no, nivel, prefixo, is_ultimo_filho):
        sb = ""
        sb += prefixo
        if nivel == 0:
            sb += "["
        else:
            sb += "└─" if is_ultimo_filho else "├─"
            sb += "["

        sb += str(no.info) + "]" + "\n"

        prefixo_filho = prefixo + ("  " if is_ultimo_filho else "│   ")

        if no.esq is not None:
            sb += self._string_recursivo(no.esq, nivel + 1, prefixo_filho, False)
        if no.dir is not None:
            sb += self._string_recursivo(no.dir, nivel + 1, prefixo_filho, True)

        return sb


if __name__ == "__main__":

    arvore = ArvoreBinaria()
    valores = [30, 50, 70, 20, 40, 60, 80]
    for valor in valores:
        arvore.inserir(valor)

    print(arvore)
    print("arvore.contem(80)", arvore.contem(80))
    print("arvore.contem(90)", arvore.contem(90))
    print("arvore.contem(50)", arvore.contem(50))

    print("arvore.profundidade(No(80))", arvore.profundidade(No(80)))
    print("arvore.profundidade(No(60))", arvore.profundidade(No(60)))

    arvore.balancear()
    print(arvore)