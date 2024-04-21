from functools import reduce


# Fáceis:
# 1. Implemente uma função que verifica se todos os elementos em um conjunto são do tipo inteiro.
# 2. Escreva um algoritmo que encontre o maior número em um conjunto.
# 3. Crie uma função que retorne um novo conjunto com os elementos invertidos de um conjunto dado.
# 4. Implemente uma função que adicione um elemento a um conjunto e retorne True se o elemento foi adicionado com sucesso.

# Médias:
# 5. Escreva uma função que determine se um conjunto é um superconjunto de outro.
# 6. Implemente uma função que retorne a união de dois conjuntos sem usar o método union.
# 7. Crie um algoritmo que encontre a interseção de três conjuntos.
# 8. Escreva uma função que simule a diferença entre dois conjuntos sem usar o método difference.

# Difíceis:
# 9. Implemente uma função que retorne conjuntos de todos os subconjuntos possíveis de um conjunto dado.
# 10. Escreva um algoritmo que verifique se dois conjuntos são disjuntos.
# 11. Crie uma função que encontre a diferença simétrica entre dois conjuntos e retorne um novo conjunto com esses elementos.
# 12. Implemente um algoritmo que remova um elemento aleatório de um conjunto até que ele esteja vazio.

# Muito Difíceis:
# 13. Escreva uma função que encontre todos os pares de elementos de dois conjuntos que somam um número específico.
# 14. Implemente um algoritmo que verifique se um conjunto é uma partição válida de outro conjunto.
# 15. Crie uma função que retorne o produto cartesiano de dois conjuntos.
# 16. Implemente um algoritmo que encontre o conjunto de todos os elementos que aparecem em apenas um dos vários conjuntos dados (diferença multi-conjunto).
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7. Crie um algoritmo que encontre a interseção de três conjuntos.
# (Faça pelo menos 1 implementação sem usar o método intersection)
def intersection_of_three_sets_1(set1, set2, set3):
    return set1.intersection_1(set2, set3)


def intersection_of_three_sets_2(set1, set2, set3):
    return set1 & set2 & set3


def intersection_of_three_sets_3(set1, set2, set3):
    # Inicializa um conjunto vazio para a interseção
    intersection = set()
    for element in set1:
        # Verifica se o elemento está presente nos outros dois conjuntos
        if element in set2 and element in set3:
            intersection.add(element)
    return intersection


def intersection_of_three_sets_4(set1, set2, set3):
    return reduce(lambda a, b: a & b, (set1, set2, set3))


def test_intersection_of_three_sets():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    set3 = {5, 6, 7, 8, 9}

    ans_1 = intersection_of_three_sets_1(set1, set2, set3)
    ans_2 = intersection_of_three_sets_2(set1, set2, set3)
    ans_3 = intersection_of_three_sets_3(set1, set2, set3)
    ans_4 = intersection_of_three_sets_4(set1, set2, set3)

    print("set1", set1)
    print("set2", set2)
    print("set3", set3)

    print("ans_1", ans_1)
    print("ans_2", ans_2)
    print("ans_3", ans_3)
    print("ans_4", ans_4)


# X. Implemente uma função que retorne a união de dois conjuntos (faça pelo menos 1 implementação sem usar o método union)
def union_of_two_sets_1(set1, set2):
    return set1 | set2


def union_of_two_sets_2(set1, set2):
    return set1.union(set2)


def union_of_two_sets_3(set1, set2):
    union_set = set()

    # Adiciona todos os elementos do primeiro conjunto
    for element in set1:
        union_set.add(element)

    # Adiciona todos os elementos do segundo conjunto, se ainda não estiverem presentes
    for element in set2:
        union_set.add(element)

    return union_set


def union_of_two_sets_4(set1, set2):
    # Utiliza compreensão de conjunto para unir os dois conjuntos
    return {element for element in set1}.union({element for element in set2})


def test_union_of_two_sets():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    ans_1 = union_of_two_sets_1(set1, set2)
    ans_2 = union_of_two_sets_2(set1, set2)
    ans_3 = union_of_two_sets_3(set1, set2)
    ans_4 = union_of_two_sets_4(set1, set2)

    print("set1", set1)
    print("set2", set2)

    print("ans_1", ans_1)
    print("ans_2", ans_2)
    print("ans_3", ans_3)
    print("ans_4", ans_4)


def main():
    test_intersection_of_three_sets()
    test_union_of_two_sets()


if __name__ == "__main__":
    main()
