import unicodedata
import re


def normalize_string(string: str) -> str:
    """
    Normaliza uma string: remove acentos, converte para minúsculas e remove caracteres não alfanuméricos.
    """
    string = (unicodedata.normalize("NFKD", string)
              .encode("ASCII", "ignore")
              .decode())  # Remove acentos
    string = string.lower()  # Converte para minúsculas
    string = re.sub(r"[^a-z0-9]", "", string)  # Remove caracteres não alfanuméricos

    return string


def is_palindrome(string: str) -> bool:
    """
    Verifica se uma string é um palíndromo, ignorando espaços, pontuações e acentos.
    """

    string = normalize_string(string)
    return string == string[::-1]


def test_is_palindrome():
    print("is_palindrome('ovo') ->", is_palindrome('ovo'))  # True
    print("is_palindrome('A cara: rajada da, jararaca') ->", is_palindrome('A cara: rajada da, jararaca'))  # True
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
