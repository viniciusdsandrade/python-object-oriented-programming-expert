import decimal


# 3. Classe Retangulo: Crie uma classe que modele um retangulo:
# a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular
# Perímetro;
# c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as
# medidades de um local. Depois, deve criar um objeto com as medidas e calcular a
# quantidade de pisos e de rodapés necessárias para o local.


class Retangulo:
    def __init__(self, largura: decimal, altura: decimal):
        self._largura = self._validar_lado(largura)
        self._altura = self._validar_lado(altura)

    @staticmethod
    def _validar_lado(lado):
        if not isinstance(lado, (int, decimal)):
            raise TypeError(f'O lado precisa ser int ou float, não {type(lado)}')
        if lado < 0:
            raise ValueError('O lado do quadrado não pode ser menor que zero.')
        return lado

    @property
    def largura(self) -> decimal:
        return self._largura

    @largura.setter
    def largura(self, valor: decimal):
        self._largura = self._validar_lado(valor)

    @property
    def altura(self) -> decimal:
        return self._altura

    @altura.setter
    def altura(self, valor: decimal):
        self._altura = self._validar_lado(valor)

    def calcular_area(self) -> decimal:
        return self._largura * self._altura

    def calcular_perimetro(self) -> decimal:
        return 2 * (self._largura + self._altura)

    def __str__(self):
        return (f'Retângulo: \n'
                f'Largura: {self.largura},\n'
                f'Altura: {self.altura},\n'
                f'Área: {self.calcular_area()},\n'
                f'Perímetro: {self.calcular_perimetro()}')


if __name__ == '__main__':
    r = Retangulo(4, 5)
    print(r)
    print(r.calcular_area())
    print(r.calcular_perimetro())
    r.largura = 5
    r.altura = 6
    print(r)
    print(r.calcular_area())
    print(r.calcular_perimetro())
    r.largura = 6
    r.altura = 7
    print(r)
    print(r.calcular_area())
    print(r.calcular_perimetro())
