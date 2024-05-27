# 7. Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho
# Eletrônico):
# a. Atributos: Nome, Fome, Saúde e Idade
# b. Métodos:
#   Alterar Nome,
#   Alterar Fome,
#   Alterar Saúde e
#   Alterar Idade
#
# Obs: Existe mais uma informação que
# devemos considerar, o Humor do nosso tamagushi, este humor é uma
# combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não
# devemos criar um atributo para armazenar esta informação por que ela pode ser
# calculada a qualquer momento.

class BichinhoVirtual:
    def __init__(self, nome: str, fome: int, saude: int, idade: int):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, nome: str):
        self.nome = nome

    def alterar_fome(self, fome: int):
        self.fome = fome

    def alterar_saude(self, saude: int):
        self.saude = saude

    def alterar_idade(self, idade: int):
        self.idade = idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    # Algoritmo para calcular o humor do bichinho
    # O humor é a soma da fome e da saúde
    def humor(self):
        return self.fome + self.saude

    def __str__(self):
        return (f'BichinhoVirtual: \n'
                f'Nome: {self.nome} - '
                f'Fome: {self.fome} - '
                f'Saúde: {self.saude} - '
                f'Idade: {self.idade} - ')
