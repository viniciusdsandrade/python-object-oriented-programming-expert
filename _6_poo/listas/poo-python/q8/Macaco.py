# 8. Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e bucho
# (estomago) e pelo menos os métodos comer(), verBucho() e digerir().

# Faça um  programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com
# pelo menos 3 alimentos diferentes e verificando o conteúdo do estômago a cada refeição.

# Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome: str):
        self.nome = self.valida_nome(nome)
        self.bucho = []

    @staticmethod
    def valida_nome(nome: str):
        if not isinstance(nome, str):
            raise ValueError("Nome deve ser uma string")
        return nome

    def comer(self, alimento: object):
        self.bucho.append(alimento)

    def verBucho(self):
        print(f"Bucho do {self.nome}: {self.bucho}")

    def digerir(self):
        self.bucho = []

    # Quero fazer um ToString tal qual mostre o nome do macaco e o que conteúdo do seu bucho
    def __str__(self):
        conteudo_bucho = []
        for item in self.bucho:
            if isinstance(item, Macaco):  # Verifica se o item é um Macaco
                conteudo_bucho.append(item.nome)  # Adiciona o nome do Macaco
            else:
                conteudo_bucho.append(item)  # Adiciona o item normalmente
        return (f"Macaco \n"
                f"  Nome: {self.nome}\n"
                f"  Bucho: {conteudo_bucho}\n")


if __name__ == "__main__":
    macaco1 = Macaco("Macaco1")
    macaco2 = Macaco("Macaco2")

    macaco1.comer("Banana")
    macaco1.comer("Maçã")
    macaco1.comer("Laranja")
    macaco1.comer(macaco2)
    print(macaco1)
