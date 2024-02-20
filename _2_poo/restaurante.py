class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.categoria = categoria
        self.nome = nome
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return (f'Nome: {self.nome}, '
                f'Categoria: {self.categoria}, '
                f'Ativo: {self.ativo}')

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False

    @staticmethod
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | '
                  f'{restaurante.categoria} | '
                  f'{restaurante.ativo}')


restaurante_praca = Restaurante('Restaurante', 'Comida Mineira')
restaurante_praca.nome = 'Restaurante da Praça'
restaurante_praca.categoria = 'Comida Mineira'
restaurante_praca.ativo = True

restaurante_pizza = Restaurante('Pizza', 'categoria')
restaurante_pizza.nome = 'Pizzaria do Gordo'
restaurante_pizza.categoria = 'Pizzaria'
restaurante_pizza.ativo = True

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_pizza)
print(vars(restaurante_pizza))
Restaurante.listar_restaurantes()
