# Fáceis:
# 1. Crie um dicionário com 5 pares de chave-valor representando frutas e seus preços por quilo.
# 2. Escreva um programa que adicione um novo par de chave-valor a um dicionário existente.
# 3. Escreva um programa que remova um item do dicionário dado uma chave.
# 4. Escreva um programa que verifique se uma chave existe em um dicionário.

# Médios:
# 5. Escreva um programa que inverta as chaves e valores em um dicionário.
# 6. Escreva um programa que combine dois dicionários, somando os valores das chaves que aparecem em ambos.
# 7. Escreva um programa que crie um novo dicionário com apenas pares de chave-valor onde o valor é maior que 10.
# 8. Escreva um programa que transforme uma lista de tuplas (chave, valor) em um dicionário.

# Difíceis:
# 9. Escreva um programa que encontre a chave com o maior valor numérico em um dicionário.
# 10. Escreva um programa que ordene um dicionário por seus valores em ordem decrescente.
# 11. Escreva um programa que filtre um dicionário removendo itens cujos valores não são únicos.
# 12. Escreva um programa que gere um dicionário onde as chaves são números entre 1 e 20 (ambos incluídos) e os valores são o quadrado das chaves.

# Muito Difíceis:
# 13. Escreva um programa que encontre todos os pares de chaves em um dicionário com o mesmo valor.
# 14. Escreva um programa que gere um dicionário onde as chaves são strings representando números binários e os valores são seus equivalentes decimais.
# 15. Escreva um programa que implemente uma função de hash simples para strings e use-a para construir um dicionário de hash.
# 16. Escreva um programa que implemente um dicionário que mantém a ordem de inserção dos itens e permite a busca por intervalo de chaves.
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5. Escreva um programa que inverta as chaves e valores em um dicionário.
def invert_dict_1(my_dict):
    return {value: key for key, value in my_dict.items()}


def invert_dict_2(my_dict):
    inverted_dict = {}
    for key, value in my_dict.items():
        inverted_dict[value] = key
    return inverted_dict


def invert_dict_3(my_dict):
    inverted_dict = {}
    for key in my_dict:
        inverted_dict[my_dict[key]] = key
    return inverted_dict


def test_invert_dict():
    dict_1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    print("dict_1:        ", dict_1)
    print("invert_dict_1: ", invert_dict_1(dict_1))

    dict_2 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    print("dict_2:        ", dict_2)
    print("invert_dict_2: ", invert_dict_2(dict_2))

    dict_3 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    print("dict_3:        ", dict_3)
    print("invert_dict_3: ", invert_dict_3(dict_3))


# 6. Escreva um programa que combine dois dicionários, somando os valores das chaves que aparecem em ambos.
def combine_dicts_1(dict_1, dict_2):
    combined_dict = dict_1.copy()
    for key, value in dict_2.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value
    return combined_dict


def combine_dicts_2(dict_1, dict_2):
    combined_dict = dict_1.copy()
    for key, value in dict_2.items():
        combined_dict[key] = combined_dict.get(key, 0) + value
    return combined_dict


def test_combine_dicts():
    dict_1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    dict_2 = {"a": 2, "b": 3, "c": 4, "d": 5, "e": 6}
    print("dict_1:          ", dict_1)
    print("dict_2:          ", dict_2)
    print("combine_dicts_1: ", combine_dicts_1(dict_1, dict_2))

    print("dict_1:          ", dict_1)
    print("dict_2:          ", dict_2)
    print("combine_dicts_2: ", combine_dicts_2(dict_1, dict_2))
    print('--------------------------------------------------')


# 8 - Escreva um programa que transforme uma lista de tuplas (chave, valor) em um dicionário.
def list_to_dict_1(my_list):
    return dict(my_list)


def list_to_dict_2(my_list):
    my_dict = {}
    for key, value in my_list:
        my_dict[key] = value
    return my_dict


def list_to_dict_3(my_list):
    my_dict = {}
    for item in my_list:
        my_dict[item[0]] = item[1]
    return my_dict


def test_list_to_dict():
    lista_1 = [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)]
    print(list_to_dict_1(lista_1))

    lista_2 = [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)]
    print(list_to_dict_2(lista_2))

    lista_3 = [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)]
    print(list_to_dict_3(lista_3))


def main():
    test_combine_dicts()
    test_list_to_dict()
    test_invert_dict()


if __name__ == "__main__":
    main()
