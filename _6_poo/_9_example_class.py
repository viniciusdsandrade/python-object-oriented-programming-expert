class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, porcentagem: float):
        self.salario += self.salario * porcentagem / 100

    def get_bonificacao(self) -> float:
        return 0.0

    def __str__(self):
        return f'{self.nome} - R$ {self.salario:.2f}'


class ControleBonificacao:

    def __init__(self):
        self._total_bonificacoes = 0

    def registra(self, funcionario: Funcionario):
        self._total_bonificacoes += funcionario.get_bonificacao()

    def get_total_bonificacoes(self) -> float:
        return self._total_bonificacoes


class Terceiro(Funcionario):
    def get_bonificacao(self) -> float:
        return self.salario * 0.10


class Estagiario(Funcionario):
    def get_bonificacao(self) -> float:
        return self.salario * 0.05


class Secretaria(Funcionario):
    def get_bonificacao(self) -> float:
        return self.salario * 0.15


class Cliente:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario


def main():
    funcionario1 = Funcionario("João", 2500)
    terceiro1 = Terceiro("Maria", 1800)
    estagiario1 = Estagiario("Pedro", 1200)
    secretaria1 = Secretaria("Ana", 2200)

    controle = ControleBonificacao()

    controle.registra(funcionario1)
    controle.registra(terceiro1)
    controle.registra(estagiario1)
    controle.registra(secretaria1)

    print(f"Funcionário: {funcionario1} - Bonificação: R$ {funcionario1.get_bonificacao():.2f}")
    print(f"Terceiro: {terceiro1} - Bonificação: R$ {terceiro1.get_bonificacao():.2f}")
    print(f"Estagiario: {estagiario1} - Bonificação: R$ {estagiario1.get_bonificacao():.2f}")
    print(f"Secretaria: {secretaria1} - Bonificação: R$ {secretaria1.get_bonificacao():.2f}")

    print(f"\nTotal de bonificações: R$ {controle.get_total_bonificacoes():.2f}")


if __name__ == "__main__":
    main()
