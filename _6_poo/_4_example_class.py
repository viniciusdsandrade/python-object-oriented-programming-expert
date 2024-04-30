import copy


class Politico:
    def __init__(self, nome=None, partido=None, estado=None, funcao=None):
        self.nome = nome
        self.partido = partido
        self.estado = estado
        self.funcao = funcao

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def partido(self) -> str:
        return self._partido

    @partido.setter
    def partido(self, partido: str):
        self._partido = partido

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, estado: str):
        self._estado = estado

    @property
    def funcao(self) -> str:
        return self._funcao

    @funcao.setter
    def funcao(self, funcao: str):
        self._funcao = funcao

    def __dict__(self):
        return {
            'nome': self.nome,
            'partido': self.partido,
            'estado': self.estado,
            'funcao': self.funcao
        }

    def __copy__(self):
        return Politico(copy.deepcopy(self.nome),
                        copy.deepcopy(self.partido),
                        copy.deepcopy(self.estado),
                        copy.deepcopy(self.funcao))

    def __hash__(self):
        return hash((self.nome, self.partido, self.estado, self.funcao))

    def __eq__(self, other):
        return (self.nome == other.nome and
                self.partido == other.partido and
                self.estado == other.estado and
                self.funcao == other.funcao)

    def __repr__(self):
        return f'{self.nome} ({self.partido}) - {self.funcao}'

    def __str__(self):
        return f"modelo: {self.nome}\npartido: {self.partido}\nestado: {self.estado}\nfuncao: {self.funcao}"


class Prefeito(Politico):
    def __init__(self, nome=None, partido=None, estado=None, funcao=None, municipio=None):
        super().__init__(nome, partido, estado, funcao)
        self.municipio = municipio

    def __dict__(self):
        return {
            'nome': self.nome,
            'partido': self.partido,
            'estado': self.estado,
            'funcao': self.funcao,
            'municipio': self.municipio
        }

    def __copy__(self):
        return Prefeito(copy.deepcopy(self.nome),
                        copy.deepcopy(self.partido),
                        copy.deepcopy(self.estado),
                        copy.deepcopy(self.funcao),
                        copy.deepcopy(self.municipio))

    def __hash__(self):
        return hash((self.nome, self.partido, self.estado, self.funcao, self.municipio))

    def __eq__(self, other):
        return (self.nome == other.nome and
                self.partido == other.partido and
                self.estado == other.estado and
                self.funcao == other.funcao and
                self.municipio == other.municipio)

    def __repr__(self):
        return f'{self.nome} ({self.partido}) - {self.funcao} ({self.municipio})'

    def __str__(self):
        return f"modelo: {self.nome}\npartido: {self.partido}\nestado: {self.estado}\nfuncao: {self.funcao}\nmunicipio: {self.municipio}"


def main():
    # Criação de objetos Politico
    politico1 = Politico("Fulano", "Partido X", "Estado Y", "Deputado")
    politico2 = Politico("Beltrana", "Partido Z", "Estado W", "Senadora")

    # Testando __str__
    print(politico1)  # Saída formatada
    print(politico2)

    # Testando __repr__
    print(repr(politico1))  # Saída concisa
    print(repr(politico2))

    # Testando __eq__
    politico3 = Politico("Fulano", "Partido X", "Estado Y", "Deputado")
    print(politico1 == politico3)  # Saída: True
    print(politico1 == politico2)  # Saída: False

    # Testando __hash__ (indiretamente via um set)
    politicos_set = {politico1, politico2, politico3}
    print(len(politicos_set))  # Saída: 2 (politico1 e politico3 são considerados iguais)

    # Testando __copy__ (deep copy)
    politico4 = politico1.__copy__()
    politico4.partido = "Partido A"
    print(politico1.partido)  # Saída: Partido X (o original não foi alterado)

    # Testando propriedades (getters e setters)
    politico1.funcao = "Ministro"
    print(politico1.funcao)  # Saída: Ministro


if __name__ == '__main__':
    main()
