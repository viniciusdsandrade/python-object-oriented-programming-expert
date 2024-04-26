import copy


# Criar uma classe chamada Carro com os seguintes atributos:
# 1 - modelo
# 2 - cor
# 3 - ano
# 4 - preco
# 5 - total_carros(deve ser um atributo de classe)
# Crie os métodos:
# set e get para cada atributo,
# um construtor,
# um método imprimir_carro e um método imprimir_total.

class Carro:
    total_carros = 0  # Atributo de class

    def __init__(self, modelo, cor, ano, preco):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preco = preco
        self.__class__.total_carros += 1

    @staticmethod
    def validar_numero_positivo(valor, nome):
        if valor < 0:
            raise ValueError(f"{nome} não pode ser negativo.")

    @property
    def modelo(self):
        return self._modelo

    @property
    def cor(self):
        return self._cor

    @property
    def ano(self):
        return self._ano

    @property
    def preco(self):
        return self._preco

    @modelo.setter
    def modelo(self, novo_modelo):
        if not isinstance(novo_modelo, str):
            raise ValueError("O modelo deve ser uma string.")
        self._modelo = novo_modelo

    @cor.setter
    def cor(self, nova_cor):
        if not isinstance(nova_cor, str):
            raise ValueError("A cor deve ser uma string.")
        self._cor = nova_cor

    @ano.setter
    def ano(self, novo_ano):
        if not isinstance(novo_ano, int):
            raise ValueError("O ano deve ser um número inteiro.")
        if novo_ano == 0:
            raise ValueError("O ano não pode ser zero.")
        self._ano = novo_ano

    @preco.setter
    def preco(self, novo_preco):
        if not isinstance(novo_preco, (int, float)):
            raise ValueError("O preço deve ser um número.")
        self.validar_numero_positivo(novo_preco, "Preço")
        self._preco = novo_preco

    @classmethod
    def imprimir_total(cls):
        print(f"Total de carros: {cls.total_carros}")

    @staticmethod
    def imprimir_total_2(self):
        print(f'Total de carros: {Carro.total_carros}')

    def __str__(self):
        """Representação legível para humanos."""
        return f"Modelo: {self.modelo}\nCor: {self.cor}\nAno: {self.ano}\nPreço: {self.preco}"

    def __repr__(self):
        """Representação oficial do objeto."""
        return f"{self.__class__.__name__}({self.modelo!r}, {self.cor!r}, {self.ano!r}, {self.preco!r})"

    def __dict__(self):
        return {
            'modelo': self.modelo,
            'cor': self.cor,
            'ano': self.ano,
            'preco': self.preco
        }

    def __eq__(self, other):
        return (self.modelo == other.modelo and
                self.cor == other.cor and
                self.ano == other.ano and
                self.preco == other.preco)

    def __hash__(self):
        return hash((
            self.modelo,
            self.cor,
            self.ano,
            self.preco))

    def __copy__(self):
        return Carro(copy.deepcopy(self.modelo),
                     copy.deepcopy(self.cor),
                     copy.deepcopy(self.ano),
                     copy.deepcopy(self.preco))

# As anotações @classmethod e @staticmethod em Python são usadas para definir métodos que não estão diretamente associados a uma instância
# de uma classe, mas ainda pertencem à classe de alguma forma. Aqui está como eles diferem:

# @classmethod: um método de classe é um método que está vinculado à classe e não à instância da classe.
# Ele pode alterar o estado da classe que se aplica em todas as instâncias.
# O primeiro parâmetro de um método de classe sempre deve ser uma referência à classe,
# que é passada automaticamente. No seu exemplo, cls é uma referência à classe Carro.

# @staticmethod: um método estático é um método que pertence à classe, mas não tem acesso a nenhum estado da classe
# ou instância. Ele não pode modificar o estado da classe ou da instância. Ele também não recebe automaticamente
# o primeiro parâmetro como uma referência à classe ou instância. No seu exemplo, imprimir_total_2
# não deveria ter self como parâmetro, pois os métodos estáticos não recebem um parâmetro de classe ou instância automaticamente.

# Em resumo, a principal diferença entre os dois é que
# um método de classe pode acessar e modificar o estado da classe,
# enquanto um método estático não pode.

# Portanto, você usaria @classmethod quando o método precisa interagir com o estado da classe,
# e @staticmethod quando o método realiza alguma operação que é independente do estado da classe ou instância.
