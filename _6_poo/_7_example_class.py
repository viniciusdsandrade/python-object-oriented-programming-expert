class Pessoa:
    TITULOS = ('Sr.', 'Sra.', 'Dr.', 'Dra.')

    def __init__(self, titulo, nome, sobrenome):
        if titulo not in self.TITULOS:
            raise ValueError(f'Título inválido: {titulo}')

        self.__titulo = titulo
        self.__nome = nome
        self.__sobrenome = sobrenome

    def isSameFamily(self, other):
        return self.__sobrenome == other.__sobrenome

    def __dict__(self):
        return {
            'titulo': self.__titulo,
            'nome': self.__nome
        }

    def __del__(self):
        print(f'{self.__titulo} {self.__nome} foi removido(a)')

    def __str__(self):
        return f'{self.__titulo} {self.__nome} {self.__sobrenome}'


def main():
    p1 = Pessoa('Sr.', 'João', 'Silva')
    p2 = Pessoa('Dra.', 'Maria', 'Silva')
    p3 = Pessoa('Sr.', 'José', 'Silva')

    print(p1)
    print(p2)
    print(p3)

    is_family1 = p1.isSameFamily(p2)
    is_family2 = p1.isSameFamily(p3)
    is_family3 = p2.isSameFamily(p3)

    print("p1.isSameFamily(p2):", is_family1)
    print("p1.isSameFamily(p3):", is_family2)
    print("p2.isSameFamily(p3):", is_family3)

    print(p1.__dict__())

    print(p1)


if __name__ == '__main__':
    main()
