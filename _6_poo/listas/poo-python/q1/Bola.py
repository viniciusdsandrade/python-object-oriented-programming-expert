import decimal


class Bola:
    # Classe Bola: Crie uma classe que modele uma bola:
    # a. Atributos: Cor, circunferência, material
    # b. Métodos: trocaCor e mostraCor
    def __init__(self, cor: str, circunferencia: decimal, material: str) -> None:
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor: str) -> None:
        self.cor = cor

    def mostraCor(self) -> str:
        return self.cor
