import unicodedata


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii.decode()


def is_palindrome(string: str) -> bool:
    string = string.lower()  # Converte para minúsculo
    string = string.replace(" ", "")  # Remove espaços
    string = remove_accents(string)  # Remove acentos

    # Verifica se é palíndromo
    return string == string[::-1]


def is_palindrome_2(string: str) -> bool:
    # Colocando todos os caracteres em minúsculo
    for i in range(len(string)):
        if 'A' <= string[i] <= 'Z':
            string = string[:i] + chr(ord(string[i]) + 32) + string[i + 1:]

    # removendo espaços manualmente
    new_string = ""
    for i in range(len(string)):
        if string[i] != " ":
            new_string += string[i]
    string = new_string

    # 'Two pointer' para verificar se é palíndromo
    for i in range(int(len(string) // 2)):
        tam = len(string) - 1
        if string[i] != string[tam - 1]:
            return False

    return True


def test_is_palindrome():
    print("Testando is_palindrome_2()")
    print("is_palindrome_2('ovo') ->", is_palindrome_2('ovo'))  # True
    print("is_palindrome_2('A cara rajada da jararaca') ->", is_palindrome_2('A cara rajada da jararaca'))  # True
    print("is_palindrome_2('Ame o Poemá') ->", is_palindrome_2('Ame o poema'))  # True
    print("is_palindrome_2('A sacada da casa') ->", is_palindrome_2('A sacada da casa'))  # True
    print("is_palindrome_2('A torre da derrota') ->", is_palindrome_2('A torre da derrota'))  # True
    print("is_palindrome_2('Subi no Onibus') ->", is_palindrome_2('Subi no Onibus'))  # True

    print("Testando is_palindrome()")
    print("is_palindrome('ovo') ->", is_palindrome('ovo'))  # True
    print("is_palindrome('A cara rajada da jararaca') ->", is_palindrome('A cara rajada da jararaca'))  # True
    print("is_palindrome('Ame o Poemá') ->", is_palindrome('Ame o poemá'))  # True
    print("is_palindrome('A sacada da casa') ->", is_palindrome('A sacada da casa'))  # True
    print("is_palindrome('A torre da derrota') ->", is_palindrome('A torre da derrota'))  # True
    print("is_palindrome('Aí, Lima falou: “Olá, família!”') ->",
          is_palindrome('Aí, Lima falou: “Olá, família!”'))  # True
    print("is_palindrome('Anotaram a data da maratona') ->", is_palindrome('Anotaram a data da maratona'))  # True
    print("is_palindrome('A pateta ama até tapa') ->", is_palindrome('A pateta ama até tapa'))  # True
    print("is_palindrome('A Rita, sobre vovô, verbos atira') ->",
          is_palindrome('A Rita, sobre vovô, verbos atira'))  # True


def main():
    test_is_palindrome()


if __name__ == "__main__":
    main()
