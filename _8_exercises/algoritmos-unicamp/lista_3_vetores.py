# 3. Escreva um programa que leia duas sequências de n e m valores inteiros, onde n  m, e
# imprima quantas vezes a primeira sequência ocorre na segunda.
# Exemplo:
# Primeira sequência: 1 0 1
# Segunda sequência: 1 1 0 1 0 1 0 0 1 1 0 1 0
# Resultado: 3

# ------------------------------------------------------------------------------------------------------

# 4. Faça um programa que leia dois conjuntos de números inteiros distintos e imprima a
# interseção destes dois conjuntos (os números presentes em ambos os conjuntos).
# Exemplo:
# Primeiro conjunto: 1 2 3 4 5
# Segundo conjunto: 2 5 7 1 9 18
# Resultado: 1 2 5

# ------------------------------------------------------------------------------------------------------

# 5. Faça um programa que leia dois conjuntos de números inteiros distintos e imprima a união
# destes conjuntos (os números presentes em pelo menos um dos conjuntos).
# Exemplo:
# Primeira conjunto: 1 2 3 4 5
# Segundo conjunto: 2 5 7 1 9 18
# Resultado: 1 2 3 4 5 7 9 18

# ------------------------------------------------------------------------------------------------------

# 6. Faça um programa que leia duas sequências de números inteiros ordenados e imprima uma
# sequência com os números ordenados das duas sequências anteriores. Você não deve usar
# o método sort.
# Exemplo:
# Primeira sequência: 1 3 5 5 7 9 10
# Segunda sequência: 2 2 4 6 8 8 10
# Resultado: 1 2 2 3 4 5 5 6 7 8 8 9 10 10

# ------------------------------------------------------------------------------------------------------

# 7. Faça um programa que calcule o produto interno de dois vetores u e v de mesmo tamanho
# n. O programa deve ler primeiramente o valor de n e em seguida deve ler duas sequências
# de mesmo tamanho de números reais e salvar cada sequência em uma lista. O programa
# eve então calcular e imprimir o produto interno dos vetores lidos.

# ------------------------------------------------------------------------------------------------------

# 8. Escreva um programa que leia uma sequência de números inteiros e os salve em uma
# lista. Em seguida o programa deve ler um outro número inteiro C. O programa deve
# então encontrar dois números de posições distintas da lista cuja multiplicação seja C e
# imprimí-los. Caso não existam tais números, o programa deve imprimir uma mensagem
# correspondente.

# Exemplo:
# Lista = [2, 4, 5, 10, 7]
# C = 35

# Resultado: 5 e 7
# Lista = [2, 4, 5, 10, 7]
# C = 25

# Resultado: não existem tais números

# ------------------------------------------------------------------------------------------------------

# 9. Escreva um programa que leia uma sequência de n números inteiros positivos maiores que
# 1 e os salve em uma lista v.
# O programa deve então imprimir um quadrado de n linhas por n colunas onde em cada
# posição (i; j), com i; j 2 f0; : : : ; n 􀀀 1g, deste quadrado deverá ser impresso 1 caso os
# números v[i] e v[j] sejam coprimos, e 0 caso contrário.
# Os pares de números v[i] e v[j] são coprimos se não há nenhum divisor d > 1 que seja
# comum a ambos. Por exemplo 15 e 8 são coprimos, pois os divisores de 8, que são 2, 4 e 8,
# não são divisores de 15. Abaixo temos um exemplo de execução do programa para n = 6
# e v = [2, 3, 4, 5, 6, 7].
# v[0] v[1] v[2] v[3] v[4] v[5]
# v[0] 0 1 0 1 0 1
# v[1] 1 0 1 1 0 1
# v[2] 0 1 0 1 0 1
# v[3] 1 1 1 0 1 1
# v[4] 0 0 0 1 0 1
# v[5] 1 1 1 1 1 0
# Note no exemplo que v[0] = 2 é coprimo de v[1] = 3, v[3] = 5 e v[5] = 7.


def __exercise_3__():
    n = int(input("Digite o tamanho da primeira sequência: "))
    m = int(input("Digite o tamanho da segunda sequência: "))

    primeira_sequencia = []
    segunda_sequencia = []

    for i in range(n):
        primeira_sequencia.append(int(input(f"Digite o {i + 1}º valor da primeira sequência: ")))

    for i in range(m):
        segunda_sequencia.append(int(input(f"Digite o {i + 1}º valor da segunda sequência: ")))
    # quero fazer com conjuntos

    contador = 0
    for i in range(m - n + 1):
        if segunda_sequencia[i:i + n] == primeira_sequencia:
            contador += 1

    print(f"Resultado: {contador}")


def __exercise_4__():
    m = int(input("Digite o tamanho do primeiro conjunto: "))
    n = int(input("Digite o tamanho do segundo conjunto: "))

    primeiro_conjunto = []
    segundo_conjunto = []

    for i in range(m):
        primeiro_conjunto.append(int(input(f"Digite o {i + 1}º valor do primeiro conjunto: ")))

    for i in range(n):
        segundo_conjunto.append(int(input(f"Digite o {i + 1}º valor do segundo conjunto: ")))

    interseccao = []
    for i in primeiro_conjunto:
        if i in segundo_conjunto:
            interseccao.append(i)

    print(f"Resultado: {interseccao}")


def __exercise_5__():
    print("Exercício 5")


def __exercise_6__():
    print("Exercício 6")


def __exercise_7__():
    print("Exercício 7")


def __exercise_8__():
    print("Exercício 8")


def __exercise_9__():
    print("Exercício 9")


def main():
    while True:
        # Display exercise options
        options = [
            "3 - Exercício 3",
            "4 - Exercício 4",
            "5 - Exercício 5",
            "6 - Exercício 6",
            "7 - Exercício 7",
            "8 - Exercício 8",
            "9 - Exercício 9",
            "sair - Para sair"
        ]
        print("Escolha o exercício que deseja executar:")
        print("\n".join(options))

        # Prompt user input
        chosen_exercise = input("Digite aqui: ")

        # Check user input
        if chosen_exercise == "sair":
            break
        elif chosen_exercise in ["3", "4", "5", "6", "7", "8", "9"]:
            execute_exercise(int(chosen_exercise))  # Execute the chosen exercise
        else:
            print("Exercício não encontrado, por favor, tente novamente.")
            continue


def execute_exercise(exercise_number):
    # This function should execute the specific exercise based on the exercise number
    # Replace these placeholders with actual function calls or implementations
    print(f"Executando o Exercício {exercise_number}")


# Entry point of the program
if __name__ == "__main__":
    main()
