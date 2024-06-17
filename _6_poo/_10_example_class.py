import re
from abc import ABC, abstractmethod


class Pessoa(ABC):
    QTD_PESSOAS = 0

    def __init__(self, nome: str, idade: int):
        self.validar_nome(nome)
        self.validar_idade(idade)

        self.__nome = nome
        self.__idade = idade
        Pessoa.QTD_PESSOAS += 1

    @staticmethod
    def validar_nome(nome: str) -> None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome deve ser uma string não vazia.")

    @staticmethod
    def validar_idade(idade: int) -> None:
        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("A idade deve ser um número inteiro positivo.")

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def idade(self) -> int:
        return self.__idade

    @abstractmethod
    def mostrar_pessoa(self):
        pass

    @staticmethod
    def mostrar_qtd_pessoas():
        print(f'Quantidade de pessoas: {Pessoa.QTD_PESSOAS}')

    @classmethod
    def obter_qtd_pessoas(cls) -> int:
        return cls.QTD_PESSOAS

    def __del__(self):
        Pessoa.QTD_PESSOAS -= 1

    def __str__(self) -> str:
        return (f'{{\n'
                f'  "nome": "{self.__nome}",\n'
                f'  "idade": {self.__idade}\n'
                f'}}')

    def __eq__(self, other) -> bool:
        if not isinstance(other, Pessoa):
            return False
        return (self.__nome == other.__nome and
                self.__idade == other.__idade)

    def __hash__(self):
        return hash((self.__nome, self.__idade))


class PessoaFisica(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: str):
        super().__init__(nome, idade)
        self.validar_cpf(cpf)
        self.__cpf = cpf

    @property
    def cpf(self) -> str:
        return self.__cpf

    def mostrar_pessoa(self):
        print(f'Nome: {self.nome} - Idade: {self.idade} - CPF: {self.cpf}')

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        cpf = re.sub(r'\D', '', cpf)
        if len(cpf) != 11: return False
        if cpf == cpf[0] * 11: return False

        for i in range(9, 11):
            soma = sum((int(cpf[num]) * (i + 1 - num)) for num in range(0, i))
            digito = ((soma * 10) % 11) % 10
            if digito != int(cpf[i]):
                return False
        return True

    def __str__(self) -> str:
        pessoa_str = super().__str__()
        return (f'{pessoa_str[:-2]}\n'
                f'  "cpf": "{self.cpf}"\n'
                f'}}')

    def __eq__(self, other) -> bool:
        if not isinstance(other, PessoaFisica):
            return False
        return super().__eq__(other) and self.cpf == other.cpf

    def __hash__(self) -> int:
        return hash((self.nome, self.idade, self.cpf))


class PessoaJuridica(Pessoa):
    def __init__(self, nome: str, idade: int, cnpj: str):
        super().__init__(nome, idade)
        if not self.validar_cnpj(cnpj):
            raise ValueError("CNPJ inválido.")
        self.__cnpj = cnpj

    @property
    def cnpj(self):
        return self.__cnpj

    def mostrar_pessoa(self):
        print(f'Nome: {self.nome} - Idade: {self.idade} - CNPJ: {self.cnpj}')

    @staticmethod
    def validar_cnpj(cnpj: str) -> bool:
        cnpj = re.sub(r'\D', '', cnpj)
        if len(cnpj) != 14: return False
        if cnpj == cnpj[0] * 14: return False

        for i in range(12, 14):
            soma = sum((int(cnpj[num]) * (i + 3 - num if num < 4 else i + 1 - num)) for num in range(0, i))
            digito = ((soma * 10) % 11) % 10
            if digito != int(cnpj[i]):
                return False
        return True

    def __str__(self):
        pessoa_str = super().__str__()
        return (f'{pessoa_str[:-2]}\n'
                f'  "cnpj": "{self.cnpj}"\n'
                f'}}')

    def __eq__(self, other):
        if not isinstance(other, PessoaJuridica):
            return False
        return super().__eq__(other) and self.cnpj == other.cnpj

    def __hash__(self):
        return hash((self.nome, self.idade, self.cnpj))


if __name__ == '__main__':
    pf1 = PessoaFisica('Vinícius dos Santos Andrade', 22, '447.841.608-76')
    print(pf1)

    pj1 = PessoaJuridica('Amazon Prime', 12, '00.000.000/0001-91')
    print(pj1)

    Pessoa.mostrar_qtd_pessoas()
