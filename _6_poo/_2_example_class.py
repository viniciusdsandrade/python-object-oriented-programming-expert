import copy
import datetime


class Pessoa:

    def __init__(self, nome, nascimento, altura):
        self.nome = nome
        self.nascimento = nascimento
        self.altura = altura

    @property
    def get_nome(self):
        return self.nome

    @property
    def getIdade(self):
        return self.nascimento

    @property
    def getAltura(self):
        return self.altura

    def setNome(self, nome):
        if not isinstance(nome, str):
            raise ValueError("O nome deve ser uma string.")
        self.nome = nome

    def setAltura(self, altura):
        if not isinstance(altura, (int, float)):
            raise ValueError("A altura deve ser um número.")
        self.altura = altura

    def setIdade(self, idade):
        if not isinstance(idade, int):
            raise ValueError("A idade deve ser um número inteiro.")
        self.nascimento = idade

    def __eq__(self, other):
        return (self.nome == other.nome and
                self.nascimento == other.nascimento and
                self.altura == other.altura)

    def __hash__(self):
        return hash((
            self.nome,
            self.nascimento,
            self.altura))

    def __str__(self):
        return (f'Pessoa('
                f'{self.nome}, '
                f'{self.nascimento}, '
                f'{self.altura}'
                f')')

    def deepcopy(self):
        return Pessoa(copy.deepcopy(self.nome),
                      copy.deepcopy(self.nascimento),
                      copy.deepcopy(self.altura))

    def __clone__(self):
        return Pessoa(self.nome,
                      self.nascimento,
                      self.altura)

    def idade(self):
        today = datetime.date.today()
        idade = (today.year -
                 self.nascimento.year -
                 ((today.month, today.day) < (self.nascimento.month, self.nascimento.day)))
        return idade


pessoa1 = Pessoa('João', datetime.date(2001, 12, 6), 1.72)
pessoa2 = Pessoa('Maria', datetime.date(1990, 1, 1), 1.80)

print(pessoa1.idade())
print(pessoa2.idade())
