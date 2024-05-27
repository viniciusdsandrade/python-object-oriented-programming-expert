import decimal


# 4. Classe Pessoa: Crie uma classe que modele uma pessoa:
# a. Atributos: nome, idade, peso e altura
# b. Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que
# nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5
# cm.

class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self._nome = self._valida_nome(nome)
        self._idade = self._valida_idade(idade)
        self._peso = self._valida_peso(peso)
        self._altura = self._valida_altura(altura)

    @staticmethod
    def _valida_nome(nome: str):
        if not isinstance(nome, str):
            raise TypeError(f'O nome precisa ser uma string, não {type(nome)}')
        return nome

    @staticmethod
    def _valida_idade(idade: int):
        if not isinstance(idade, int):
            raise TypeError(f'A idade precisa ser um número inteiro, não {type(idade)}')
        if idade < 0:
            raise ValueError('A idade da pessoa não pode ser menor que zero.')
        return idade

    @staticmethod
    def _valida_peso(peso: decimal):
        if not isinstance(peso, (int, float, decimal)):
            raise TypeError(f'O peso precisa ser um número, não {type(peso)}')
        if peso < 0:
            raise ValueError('O peso da pessoa não pode ser menor que zero.')
        return peso

    @staticmethod
    def _valida_altura(altura: decimal):
        if not isinstance(altura, (int, float, decimal)):
            raise TypeError(f'A altura precisa ser um número, não {type(altura)}')
        if altura < 0:
            raise ValueError('A altura da pessoa não pode ser menor que zero.')
        return altura

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def idade(self) -> int:
        return self._idade

    @property
    def peso(self) -> float:
        return self._peso

    @property
    def altura(self) -> float:
        return self._altura

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = self._valida_nome(nome)

    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = self._valida_idade(idade)

    @peso.setter
    def peso(self, peso: float) -> None:
        self._peso = self._valida_peso(peso)

    @altura.setter
    def altura(self, altura: float) -> None:
        self._altura = self._valida_altura(altura)

    def muda_peso(self, peso: decimal) -> None:
        self._peso = self._valida_peso(peso)

    def muda_altura(self, altura: decimal) -> None:
        self._altura = self._valida_altura(altura)

    def muda_nome(self, nome: str) -> None:
        self._nome = self._valida_nome(nome)

    def muda_idade(self, idade: int) -> None:
        self._idade = self._valida_idade(idade)

    def _crescer(self, altura: decimal) -> None:
        self._altura = self._valida_altura(self._altura + altura)

    def engordar(self, peso: decimal) -> None:
        self._peso = self._valida_peso(self._peso + peso)

    def envelhecer(self, anos: int) -> None:
        self._idade = self._valida_idade(self._idade + anos)
        if self._idade < 21:
            self._crescer(0.5)

    def emagrecer(self, peso: decimal) -> None:
        self._peso = self._valida_peso(self._peso - peso)

    def __str__(self) -> str:
        return (f'Pessoa: \n'
                f'  Nome: {self._nome}\n'
                f'  Idade: {self._idade}\n'
                f'  Peso: {self._peso}\n'
                f'  Altura: {self._altura}')


if __name__ == '__main__':
    pessoa = Pessoa('João', 20, 70, 1.70)
    print(pessoa)
    pessoa.envelhecer(1)
    pessoa.engordar(5)
    pessoa.emagrecer(3)
    print(pessoa)
    pessoa.muda_nome('Maria')
    pessoa.muda_idade(25)
    pessoa.muda_peso(60)
    pessoa.muda_altura(1.65)
