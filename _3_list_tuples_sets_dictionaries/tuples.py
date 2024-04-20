import statistics
from functools import reduce
import heapq


# Fáceis:
# 1. Dada uma tupla, escreva uma função para encontrar o maior número.
# 2. Dada uma tupla, escreva uma função para encontrar o menor número.
# 3. Dada uma tupla, escreva uma função para calcular a soma dos elementos.
# 4. Dada uma tupla, escreva uma função para calcular a média dos elementos.

# Médios:
# 5. Dada uma tupla de tuplas, escreva uma função para encontrar o maior número em cada sub-tupla.
# 6. Dada uma tupla de tuplas, escreva uma função para encontrar o menor número em cada sub-tupla.
# 7. Dada uma tupla de tuplas, escreva uma função para calcular a soma dos elementos em cada sub-tupla.
# 8. Dada uma tupla de tuplas, escreva uma função para calcular a média dos elementos em cada sub-tupla.
#
# Difíceis:
# 9. Dada uma tupla de tuplas representando uma matriz quadrada, escreva uma função para calcular a soma da diagonal principal.
# 10. Dada uma tupla de tuplas representando uma matriz quadrada, escreva uma função para calcular a média da diagonal secundária.
# 11. Dada uma tupla de tuplas, escreva uma função para transpor a matriz.
# 12. Dada uma tupla de tuplas, escreva uma função para encontrar a soma dos elementos acima da diagonal principal.
#
# Muito Difíceis:
# 13. Dada uma tupla de tuplas, escreva uma função para verificar se a matriz é simétrica.
# 14. Dada uma tupla de tuplas, escreva uma função para calcular o determinante da matriz.
# 15. Dada uma tupla de tuplas, escreva uma função para encontrar a matriz inversa, se existir.
# 16. Dada uma tupla de tuplas, escreva uma função para encontrar todos os pares de números que somam um valor específico dentro da matriz.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5. Dada uma tupla de tuplas, escreva uma função para encontrar o maior número em cada sub-tupla.
def maior_elemento_sub_tupla_1(tupla: tuple) -> list:
    maior = []
    for i in range(len(tupla)):
        maior.append(max(tupla[i]))
    return maior


def maior_elemento_sub_tupla_2(tupla: tuple) -> list:
    return [max(sub_tupla) for sub_tupla in tupla]


def maior_elemento_sub_tupla_3(tupla: tuple) -> list:
    return list(map(max, tupla))


def maior_elemento_sub_tupla_4(tupla: tuple) -> list:
    return list(map(lambda sub_tupla: max(sub_tupla), tupla))


def maior_elemento_sub_tupla_5(tupla: tuple) -> list:
    return [reduce(lambda a, b: a if a > b else b, sub_tupla) for sub_tupla in tupla]


def maior_elemento_sub_tupla_6(tupla: tuple) -> list:
    return [heapq.nlargest(1, sub_tupla)[0] for sub_tupla in tupla]


def test_maior_elemento_sub_tupla():
    tupla_1 = ((1, 2, 3),
               (4, 5, 6),
               (7, 8, 9))

    tupla_2 = ((1, 2, 3),
               (4, 5, 6),
               (7, 8, 9))

    tupla_3 = ((1, 2, 3),
               (4, 5, 6),
               (7, 8, 9))

    tupla_4 = ((1, 2, 3),
               (4, 5, 6),
               (7, 8, 9))

    tupla_5 = ((1, 2, 3),
               (4, 5, 6),
               (7, 8, 9))

    tupla_6 = ((1, 2, 3),
               (4, 5, 6),
               (7, 8, 9))

    print("\ntupla_1: ")
    print_tupla(tupla_1)
    answer_1 = maior_elemento_sub_tupla_1(tupla_1)
    print("answer_1: ", answer_1)

    print("\ntupla_2: ")
    print_tupla(tupla_2)
    answer_2 = maior_elemento_sub_tupla_2(tupla_2)
    print("answer_2: ", answer_2)

    print("\ntupla_3: ")
    print_tupla(tupla_3)
    answer_3 = maior_elemento_sub_tupla_3(tupla_3)
    print("answer_3: ", answer_3)

    print("\ntupla_4: ")
    print_tupla(tupla_4)
    answer_4 = maior_elemento_sub_tupla_4(tupla_4)
    print("answer_4: ", answer_4)

    print("\ntupla_5: ")
    print_tupla(tupla_5)
    answer_5 = maior_elemento_sub_tupla_5(tupla_5)
    print("answer_5: ", answer_5)

    print("\ntupla_6: ")
    print_tupla(tupla_6)
    answer_6 = maior_elemento_sub_tupla_6(tupla_6)
    print("answer_6: ", answer_6)


# 8. Dada uma tupla de tuplas, escreva uma função para calcular a média dos elementos em cada sub-tupla.
def media_elemento_sub_tupla_1(tupla: tuple) -> list:
    return [sum(sub_tupla) / len(sub_tupla) for sub_tupla in tupla]


def media_elemento_sub_tupla_2(tupla: tuple) -> list:
    return list(map(lambda sub_tupla: sum(sub_tupla) / len(sub_tupla), tupla))


def media_elemento_sub_tupla_3(tupla: tuple) -> list:
    medias = []
    for sub_tupla in tupla:
        total = sum(sub_tupla)
        media = total / len(sub_tupla)
        medias.append(media)
    return medias


def media_elemento_sub_tupla_4(tupla: tuple) -> list:
    return [statistics.mean(sub_tupla) for sub_tupla in tupla]


def test_media_elemento_sub_tupla():
    tupla_1 = ((1, 2, 3),
               (4, 5, 6),
               (7, 8, 9))

    tupla_2 = ((1, 2, 3),
               (4, 5, 6),
               (7, 8, 9))

    tupla_3 = ((1, 2, 3),
               (4, 5, 6),
               (7, 8, 9))

    tupla_4 = ((1, 2, 3),
               (4, 5, 6),
               (7, 8, 9))

    print("\ntupla_1: ")
    print_tupla(tupla_1)
    answer_1 = media_elemento_sub_tupla_1(tupla_1)
    print("answer_1: ", answer_1)

    print("\ntupla_2: ")
    print_tupla(tupla_2)
    answer_2 = media_elemento_sub_tupla_2(tupla_2)
    print("answer_2: ", answer_2)

    print("\ntupla_3: ")
    print_tupla(tupla_3)
    answer_3 = media_elemento_sub_tupla_3(tupla_3)
    print("answer_3: ", answer_3)

    print("\ntupla_4: ")
    print_tupla(tupla_4)
    answer_4 = media_elemento_sub_tupla_4(tupla_4)
    print("answer_4: ", answer_4)


def print_tupla(tupla: tuple):
    for i in range(len(tupla)):
        print(tupla[i])


def main():
    test_media_elemento_sub_tupla()


if __name__ == '__main__':
    main()
