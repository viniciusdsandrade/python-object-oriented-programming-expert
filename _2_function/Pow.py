import math


def myPow1(x: float, n: int) -> float:
    return x ** n


def myPow2(x: float, n: int) -> float:
    return pow(x, n)


def myPow3(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    elif n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    for _ in range(n):
        result *= x
    return result


def myPow4(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    elif n < 0:
        return 1 / myPow4(x, -n)
    elif n % 2 == 0:
        return myPow4(x * x, n // 2)
    else:
        return x * myPow4(x * x, (n - 1) // 2)


def myPow5(x: float, n: int) -> float:
    return math.pow(x, n) if n >= 0 else 1 / math.pow(x, -n)


def test_myPow():
    base_exponent = [(2, 3), (3, 2), (2, -3), (0, 1), (1, 0),
                     (-2, 3), (-3, 2), (-2, -3), (0, 0),
                     (2.5, 2), (1.2, -2), (-0.5, 3)]
    for base in base_exponent:
        print(f"myPow1({base[0]}, {base[1]}) ->", myPow1(*base))
        print(f"myPow2({base[0]}, {base[1]}) ->", myPow2(*base))
        print(f"myPow3({base[0]}, {base[1]}) ->", myPow3(*base))
        print(f"myPow4({base[0]}, {base[1]}) ->", myPow4(*base))
        print(f"myPow5({base[0]}, {base[1]}) ->", myPow5(*base))
        print()


def main():
    test_myPow()


if __name__ == "__main__":
    main()
