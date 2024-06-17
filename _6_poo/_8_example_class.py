import copy
import decimal
from typing import Tuple, Dict


class Numeros:
    MULTIPLIER = 13

    def __init__(self, x: decimal, y: decimal) -> None:
        if not isinstance(x, (int, decimal)):
            raise TypeError(f'x precisa ser int ou float, não {type(x)}')
        if not isinstance(y, (int, decimal)):
            raise TypeError(f'y precisa ser int ou float, não {type(y)}')
        self.x = x
        self.y = y

    def soma(self) -> decimal:
        return self.x + self.y

    def subtrai(self) -> decimal:
        return self.x - self.y

    def divide(self) -> decimal:
        if self.y == 0:
            raise ValueError('y não pode ser 0')
        return self.x / self.y

    @property
    def x(self) -> decimal:
        return self._x

    @x.setter
    def x(self, x: decimal) -> None:
        if not isinstance(x, (int, decimal)):
            raise TypeError(f'x precisa ser int ou decimal, não {type(x)}')
        self._x = x

    @property
    def y(self) -> decimal:
        return self._y

    @y.setter
    def y(self, y: decimal) -> None:
        if not isinstance(y, (int, decimal)):
            raise TypeError(f'y precisa ser int ou decimal, não {type(y)}')
        self._y = y

    @classmethod
    def multiplica(cls, a: float) -> decimal:
        return a * cls.MULTIPLIER

    @property
    def valor(self) -> Tuple[decimal, decimal]:
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
        return hash(self.x, self.y)

    def __dict__(self) -> Dict[str, decimal]:
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
