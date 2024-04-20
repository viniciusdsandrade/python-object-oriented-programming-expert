import numpy as np


# Fáceis:
# Problema 1: Dada uma lista 2D, escreva um programa para encontrar o maior número em cada linha.
# Problema 2: Dada uma lista 2D, escreva um programa para encontrar o menor número em cada coluna.
# Problema 3: Dada uma lista 2D, escreva um programa para encontrar a soma de todos os números em cada linha.
# Problema 4: Dada uma lista 2D, escreva um programa para encontrar a média dos números em cada coluna.

# Médios:
# Problema 5: Dada uma lista 2D, escreva um programa para encontrar a diagonal principal e calcular a soma dos seus elementos.
# Problema 6: Dada uma lista 2D, escreva um programa para encontrar a diagonal secundária e calcular a média dos seus elementos.
# Problema 7: Dada uma lista 2D, escreva um programa para verificar se a matriz é uma matriz de permutação.
# Problema 8: Dada uma lista 2D, escreva um programa para rotacionar a matriz em 90 graus no sentido horário.
#
# Difíceis:
#  Problema 9: Dada uma lista 2D, escreva um programa para calcular o produto escalar de duas matrizes.
#  Problema 10: Dada uma lista 2D, escreva um programa para encontrar a matriz elevada à potência n, onde n é um número inteiro.
#  Problema 11: Dada uma lista 2D, escreva um programa para encontrar todos os elementos únicos e suas contagens.
#  Problema 12: Dada uma lista 2D, escreva um programa para encontrar a matriz resultante após realizar a operação de convolução com um kernel dado.
#
# Avançados:
# Problema 13: Dada uma lista 2D, escreva um programa para encontrar o traço da matriz (a soma dos elementos da diagonal principal).
# Problema 14: Dada uma lista 2D, escreva um programa para encontrar a submatriz com a maior soma (problema da submatriz máxima).
# Problema 15: Dada uma lista 2D, escreva um programa para encontrar a matriz triangular superior resultante da decomposição LU.
# Problema 16: Dada uma lista 2D, escreva um programa para encontrar o vetor próprio correspondente ao maior valor próprio da matriz.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Problema 8: Dada uma lista 2D, escreva um programa para rotacionar a matriz em 90 graus no sentido horário.
def rotate_matrix_1(matrix) -> list:
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
    return matrix


# Versão 2: Usando compreensão de lista e zip
def rotate_matrix_2(matrix) -> list:
    return [list(t) for t in zip(*matrix[::-1])]


# Versão 3: Usando a função reversed e zip
def rotate_matrix_3(matrix) -> list:
    return [list(t) for t in zip(*reversed(matrix))]


def test_rotate_matrix():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print("Original Matrix:")
    print_matrix(matrix)

    rotated_matrix_2 = rotate_matrix_2(matrix)
    print("rotated_matrix_2")
    print_matrix(rotated_matrix_2)

    rotated_matrix_3 = rotate_matrix_3(matrix)
    print("rotated_matrix_3")
    print_matrix(rotated_matrix_3)

    rotated_matrix_1 = rotate_matrix_1(matrix)
    print("rotated_matrix_1")
    print_matrix(rotated_matrix_1)


#  Problema 9: Dada uma lista 2D, escreva um programa para calcular o produto escalar de duas matrizes.
def matrix_multiplication_1(matrix1, matrix2):
    m1, n1 = len(matrix1), len(matrix1[0])
    m2, n2 = len(matrix2), len(matrix2[0])

    if n1 != m2:
        return "As matrizes não podem ser multiplicadas."

    result = [[0 for _ in range(n2)] for _ in range(m1)]

    for i in range(m1):
        for j in range(n2):
            for k in range(n1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def matrix_multiplication_2(matrix1, matrix2):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]


def matrix_multiplication_3(matrix1, matrix2):
    return np.dot(matrix1, matrix2).tolist()


# Versão 4: Multiplicação de matrizes sem numpy, otimizada com list comprehension
def matrix_multiplication_4(matrix1, matrix2):
    m1, n1 = len(matrix1), len(matrix1[0])
    m2, n2 = len(matrix2), len(matrix2[0])
    if n1 != m2:
        return "As matrizes não podem ser multiplicadas."

    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(n1)) for j in range(n2)] for i in range(m1)]
    return result


def test_matrix_multiplication():
    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

    matrix2 = [[1, 2],
               [3, 4],
               [5, 6]]

    print("Matrix 1:")
    print_matrix(matrix1)
    print("Matrix 2:")
    print_matrix(matrix2)

    result_1 = matrix_multiplication_1(matrix1, matrix2)
    print("Result 1:")
    print_matrix(result_1)

    result_2 = matrix_multiplication_2(matrix1, matrix2)
    print("Result 2:")
    print_matrix(result_2)

    result_3 = matrix_multiplication_3(matrix1, matrix2)
    print("Result 3:")
    print_matrix(result_3)

    result_4 = matrix_multiplication_4(matrix1, matrix2)
    print("Result 4:")
    print_matrix(result_4)


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def main():
    test_rotate_matrix()
    test_matrix_multiplication()


if __name__ == "__main__":
    main()
