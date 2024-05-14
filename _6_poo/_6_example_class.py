from copy import deepcopy


class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: str):
        self._nome = nome  # _ is a convention to indicate that the attribute is private
        self._idade = idade
        self._sexo = sexo

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def idade(self) -> int:
        return self._idade

    @property
    def sexo(self) -> str:
        return self._sexo

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade

    @sexo.setter
    def sexo(self, sexo: str) -> None:
        self._sexo = sexo

    def __copy__(self) -> __init__:
        return Pessoa(
            deepcopy(self._nome),
            deepcopy(self._idade),
            deepcopy(self._sexo)
        )

    def __eq__(self, other) -> bool:
        return (self.nome == other.nome and
                self.idade == other.idade and
                self.sexo == other.sexo)

    def __hash__(self) -> int:
        return hash((self.nome, self.idade, self.sexo))

    def __dict__(self) -> dict:
        return {
            'nome': self.nome,
            'idade': self.idade,
            'sexo': self.sexo
        }

    def __str__(self) -> str:
        return f'Nome: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}'


class Aluno(Pessoa):
    _registry = []

    def __init__(self, nome: str, idade: int, sexo: str, ra: str):
        super().__init__(nome, idade, sexo)
        self._ra = ra
        self._registry.append(self)

    @property
    def ra(self) -> str:
        return self._ra

    @ra.setter
    def ra(self, ra: str) -> None:
        self._ra = ra

    def __dict__(self) -> dict:
        dicionario = super().__dict__()
        dicionario['ra'] = self.ra
        return dicionario

    def __eq__(self, other) -> bool:
        return self.ra == other.ra

    def __hash__(self) -> int:
        return hash(self.ra)

    def __copy__(self) -> __init__:
        return Aluno(
            deepcopy(self._nome),
            deepcopy(self._idade),
            deepcopy(self._sexo),
            deepcopy(self._ra)
        )

    def __str__(self) -> str:
        return f'{super().__str__()}, RA: {self.ra}'

    @classmethod
    def create(cls, nome: str, idade: int, sexo: str, ra: str):
        return cls(nome, idade, sexo, ra)

    @classmethod
    def read(cls, ra: str):
        for aluno in cls._registry:
            if aluno.ra == ra:
                return aluno
        return None

    @classmethod
    def read_all(cls):
        return cls._registry

    @classmethod
    def update(cls, ra: str, nome: str = None, idade: int = None, sexo: str = None, new_ra: str = None):
        aluno = cls.read(ra)
        if aluno is not None:
            if nome is not None: aluno._nome = nome
            if idade is not None: aluno._idade = idade
            if sexo is not None: aluno._sexo = sexo
            if new_ra is not None: aluno._ra = new_ra
            return True
        return False

    @classmethod
    def delete(cls, ra: str) -> bool:
        aluno = cls.read(ra)
        if aluno is not None:
            cls._registry.remove(aluno)
            return True
        return False

    @classmethod
    def delete_all(cls):
        cls._registry.clear()


def main():
    aluno1 = Aluno.create("João", 20, "M", "RA001")
    aluno2 = Aluno.create("Maria", 22, "F", "RA002")
    aluno3 = Aluno.create("Carlos", 21, "M", "RA003")

    for aluno in Aluno.read_all():
        print(aluno)

    print(Aluno.read("RA001"))

    Aluno.update("RA002", nome="Ana", idade=23)
    print(Aluno.read("RA002"))

    Aluno.delete("RA003")
    print(Aluno.read("RA003"))


if __name__ == '__main__':
    main()
