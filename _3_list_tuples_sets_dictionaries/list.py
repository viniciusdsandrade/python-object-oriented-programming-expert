# Fáceis:
# 1. Crie uma lista com os primeiros 10 números inteiros e imprima-a.
# 2. Escreva um programa que adicione um elemento ao final de uma lista existente.
# 3. Escreva um programa que remova o último elemento de uma lista.
# 4. Escreva um programa que verifique se um elemento existe em uma lista.

# Médios:
# 5. Escreva um programa que encontre o segundo maior número em uma lista.
# 6. Escreva um programa que remova todos os elementos duplicados de uma lista.
# 7. Escreva um programa que insira um elemento em uma posição específica de uma lista.
# 8. Escreva um programa que concatene duas listas elemento a elemento em uma nova lista.

# Difíceis:
# 9. Escreva um programa que rotacione os elementos de uma lista para a esquerda n vezes.
# 10. Escreva um programa que calcule a diferença entre o maior e o menor valor em uma lista.
# 11. Escreva um programa que substitua todos os números negativos por zero em uma lista.
# 12. Escreva um programa que encontre todos os pares de números em uma lista cuja soma é igual a um número dado.

# Muito Difíceis:
# 13. Escreva um programa que encontre todos os subconjuntos de uma lista cuja soma dos elementos é igual a um número dado.
# 14. Escreva um programa que implemente o algoritmo de ordenação “merge sort” em uma lista.
# 15. Escreva um programa que determine se uma lista é um palíndromo.
# 16. Escreva um programa que encontre a sequência contínua mais longa de números positivos em uma lista.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 9. Escreva um programa que rotacione os elementos de uma lista para a esquerda n vezes.
def rotate_left_1(lst, n):
    for _ in range(n):
        lst.append(lst.pop(0))
    return lst


def rotate_left_2(lst, n):
    return lst[n:] + lst[:n]


def rotate_left_3(lst, n):
    return lst[n % len(lst):] + lst[:n % len(lst)]


def test_rotate_left():
    lista = [1, 2, 3, 4, 5]
    print("lista original:", lista)

    rotate_1 = rotate_left_1(lista, 2)
    print("rotate_left_1:", rotate_1)

    rotate_2 = rotate_left_2(lista, 2)
    print("rotate_left_2:", rotate_2)

    rotate_3 = rotate_left_3(lista, 2)
    print("rotate_left_3:", rotate_3)


# 10. Escreva um programa que calcule a diferença entre o maior e o menor valor em uma lista.
def difference_1(lst):
    return max(lst) - min(lst)


def difference_2(lst):
    return sorted(lst)[-1] - sorted(lst)[0]


def difference_3(lst):
    return max(lst, default=0) - min(lst, default=0)


def difference_4(lst):
    return max(lst or [0]) - min(lst or [0])


def test_difference():
    lista = [1, 2, 3, 4, 5]
    print("lista original:", lista)

    diff_1 = difference_1(lista)
    print("difference_1:", diff_1)

    diff_2 = difference_2(lista)
    print("difference_2:", diff_2)

    diff_3 = difference_3(lista)
    print("difference_3:", diff_3)

    diff_4 = difference_4(lista)
    print("difference_4:", diff_4)


def main():
    test_rotate_left()
    test_difference()


if __name__ == '__main__':
    main()
