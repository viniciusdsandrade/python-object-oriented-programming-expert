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
    total_carros = 0  # atributo de classe

    def __init__(self, modelo, cor, ano, preco):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preco = preco
        Carro.total_carros += 17

    def get_modelo(self):
        return self.modelo

    def get_cor(self):
        return self.cor

    def get_ano(self):
        return self.ano

    def get_preco(self):
        return self.preco

    def set_modelo(self, modelo):
        if not isinstance(modelo, str):
            raise ValueError("O modelo deve ser uma string.")
        self.modelo = modelo

    def set_cor(self, cor):
        if not isinstance(cor, str):
            raise ValueError("A cor deve ser uma string.")
        self.cor = cor

    def set_ano(self, ano):
        if not isinstance(ano, int):
            raise ValueError("O ano deve ser um número inteiro.")
        self.ano = ano

    def set_preco(self, preco):
        if not isinstance(preco, (int, float)):
            raise ValueError("O preço deve ser um número.")
        self.preco = preco

    def imprimir_carro(self):
        print(f'Modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Ano: {self.ano}')
        print(f'Preço: {self.preco}')

    # As anotações @classmethod e @staticmethod em Python são usadas para definir métodos que não estão diretamente associados a uma instância de uma classe, mas ainda pertencem à classe de alguma forma. Aqui está como eles diferem:

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
    @classmethod
    def imprimir_total(cls):
        print(f'Total de carros: {Carro.total_carros}')

    @staticmethod
    def imprimir_total_2(self):
        print(f'Total de carros: {Carro.total_carros}')

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

    def __str__(self):
        return (f'Carro('
                f'{self.modelo}, '
                f'{self.cor}, '
                f'{self.ano}, '
                f'{self.preco}'
                f')')

    def clone(self):
        return Carro(copy.deepcopy(self.modelo),
                     copy.deepcopy(self.cor),
                     copy.deepcopy(self.ano),
                     copy.deepcopy(self.preco))
