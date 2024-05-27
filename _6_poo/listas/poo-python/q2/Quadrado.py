import decimal


# 2. Classe Quadrado: Crie uma classe que modele um quadrado:
# a. Atributos: Tamanho do lado
# b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;


class Quadrado:
    def __init__(self, lado: decimal):
        self._lado = self._validar_lado(lado)

    @staticmethod
    def _validar_lado(lado):
        if not isinstance(lado, (int, float)):
            raise TypeError(f'O lado precisa ser int ou float, não {type(lado)}')
        if lado < 0:
            raise ValueError('O lado do quadrado não pode ser menor que zero.')
        return lado

    @property
    def lado(self) -> decimal:
        return self._lado

    @lado.setter
    def lado(self, valor: decimal):
        self._lado = self._validar_lado(valor)

    def calcular_area(self) -> decimal:
        return self._lado ** 2

    def calcular_perimetro(self) -> decimal:
        return self._lado * 4

    def __str__(self):
        return (f'Quadrado: \n'
                f'Lado: {self.lado},\n'
                f'Área: {self.calcular_area()},\n'
                f'Perímetro: {self.calcular_perimetro()}')


if __name__ == '__main__':
    q = Quadrado(4)
    print(q)
    print(q.calcular_area())
    print(q.calcular_perimetro())
    q.lado = 5
    print(q)
    print(q.calcular_area())
    print(q.calcular_perimetro())
    q.lado = 6
    print(q)
