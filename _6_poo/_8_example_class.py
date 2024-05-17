# Crie uma classe chamada 'Numeros' que possui um único atributo de classe chamad 'MULTIPLIER' e um construtor que
# usa os parâmetros 'x' e 'y' (todos devem ser numeros)
from typing import Tuple


class Numeros:
    MULTIPLIER = 13

    def __init__(self, x: float, y: float):
        if not isinstance(x, (int, float)):
            raise TypeError(f'x precisa ser int ou float, não {type(x)}')
        if not isinstance(y, (int, float)):
            raise TypeError(f'y precisa ser int ou float, não {type(y)}')
        self.x = x
        self.y = y

    def soma(self) -> float:
        """Retorna a soma dos atributos 'x' e 'y'."""
        return self.x + self.y

    @classmethod
    def multiplica(cls, a: float) -> float:
        """Retorna o produto de 'a' e MULTIPLIER."""
        return a * cls.MULTIPLIER

    @property
    def valor(self) -> Tuple[float, float]:
        """Retorna uma tupla contendo os valores de 'x' e 'y'."""
        return self.x, self.y


def main():
    n = Numeros(2, 3)
    print(n.soma())
    print(n.multiplica(2))
    print(n.valor)


if __name__ == '__main__':
    main()
