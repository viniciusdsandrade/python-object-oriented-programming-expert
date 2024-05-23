# Crie uma classe chamada 'Numeros' que possui um único atributo de classe chamad 'MULTIPLIER' e um construtor que
# usa os parâmetros 'x' e 'y' (todos devem ser numeros)
import copy
import decimal
from typing import Tuple, Dict


class Numeros:
    MULTIPLIER = 13

    def __init__(self, x: decimal, y: decimal) -> None:
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

    def __repr__(self) -> str:
        return f'Numeros({self.x}, {self.y})'

    def __copy__(self) -> __init__:
        return Numeros(copy.deepcopy(self.x),
                       copy.deepcopy(self.y),
                       copy.deepcopy(self.MULTIPLIER))

    def __eq__(self, other) -> bool:
        return (self.x == other.x and
                self.y == other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __dict__(self) -> Dict[str, float]:
        return {'x': self.x, 'y': self.y}

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


def main():
    n = Numeros(2, 3)
    print(n.soma())
    print(n.multiplica(2))
    print(n.valor)


if __name__ == '__main__':
    main()
