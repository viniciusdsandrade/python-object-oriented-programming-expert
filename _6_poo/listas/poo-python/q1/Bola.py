import decimal
import math


# Classe Bola: Crie uma classe que modele uma bola:
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor


class Bola:
    def __init__(self, cor: str, circunferencia: decimal, material: str):
        self._cor = self._valida_cor(cor)
        self._circunferencia = self._valida_circunferencia(circunferencia)
        self._material = self._valida_material(material)

    @staticmethod
    def _valida_cor(cor: str):
        if not isinstance(cor, str):
            raise TypeError(f'A cor precisa ser uma string, não {type(cor)}')
        return cor

    @staticmethod
    def _valida_circunferencia(circunferencia):  # Aceite float como entrada
        if not isinstance(circunferencia, (int, float)):
            raise TypeError(f'A circunferência precisa ser um número, não {type(circunferencia)}')
        if circunferencia < 0:
            raise ValueError('A circunferência da bola não pode ser menor que zero.')
        return circunferencia  # Converta para Decimal aqui

    @staticmethod
    def _valida_material(material: str):
        if not isinstance(material, str):
            raise TypeError(f'O material precisa ser uma string, não {type(material)}')
        return material

    @property
    def cor(self) -> str:
        return self._cor

    @property
    def circunferencia(self) -> decimal:
        return self._circunferencia

    @property
    def material(self) -> str:
        return self._material

    @property
    def raio(self) -> decimal:
        return self.circunferencia / (2 * math.pi)

    @cor.setter
    def cor(self, cor: str) -> None:
        if not isinstance(cor, str):
            raise TypeError(f'A cor precisa ser uma string, não {type(cor)}')
        self._cor = cor

    @circunferencia.setter
    def circunferencia(self, circunferencia: decimal) -> None:
        if not isinstance(circunferencia, (int, decimal)):
            raise TypeError(f'A circunferência precisa ser um decimal, não {type(circunferencia)}')
        if circunferencia < 0:
            raise ValueError('A circunferência da bola não pode ser menor que zero.')
        self._circunferencia = circunferencia

    @material.setter
    def material(self, material: str) -> None:
        if not isinstance(material, str):
            raise TypeError(f'O material precisa ser uma string, não {type(material)}')
        self._material = material

    def area(self) -> decimal:
        return 4 * math.pi * self.raio ** 2

    def volume(self) -> decimal:
        return 4 / 3 * math.pi * self.raio ** 3

    def trocaCor(self, cor: str) -> None:
        self.cor = self._valida_cor(cor)

    def trocaCircunferencia(self, circunferencia: decimal) -> None:
        self.circunferencia = self._valida_circunferencia(circunferencia)

    def trocaMaterial(self, material: str) -> None:
        self.material = self._valida_material(material)

    def mostraCor(self) -> str:
        return self.cor

    def mostraCircunferencia(self) -> decimal:
        return self.circunferencia

    def mostraMaterial(self) -> str:
        return self.material

    def __str__(self) -> str:
        return (f'Bola: \n'
                f' Cor: {self.cor},\n'
                f' Circunferência: {self.circunferencia},\n'
                f' Material: {self.material}')


if __name__ == '__main__':
    bola = Bola('Azul', 10.0, 'Plástico')
    print(bola)
    bola.trocaCor('Vermelho')
    print(bola)
    print(bola.mostraCor())
    bola.cor = 'Verde'
    print(bola)
    print(bola.mostraCor())
