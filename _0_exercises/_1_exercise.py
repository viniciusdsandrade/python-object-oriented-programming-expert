# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número,
# indo de 1 a 10.

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco
# try-except para lidar com possíveis exceções.

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a
# divisão por zero, caso a lista esteja vazia.

def listar_numeros_de_1_a_10():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numeros)


def percorrer_lista():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for numero in numeros:
        print(numero)


def numeros_em_ordem_crescente():
    for numero in range(10, 0, -1):
        print(numero)


def tabuada():
    numero = int(input('Digite um número: '))
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')


def calcular_soma_de_elementos():
    soma = 0
    for i in range(0, 11):
        soma = soma + i
    print(soma)


# Função que recebe uma lista como parâmetro de números e calcula a média
def calcular_media(numeros):
    try:
        media = sum(numeros) / len(numeros)
        print(media)
    except ZeroDivisionError:
        print('A lista está vazia')


listar_numeros_de_1_a_10()
percorrer_lista()
numeros_em_ordem_crescente()
tabuada()
calcular_soma_de_elementos()
calcular_media([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
