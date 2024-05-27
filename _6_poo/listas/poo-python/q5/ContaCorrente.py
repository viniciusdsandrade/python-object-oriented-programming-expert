import decimal


# 5. Classe Conta Corrente: Crie uma classe para implementar uma conta-corrente. A classe
# deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os
# métodos são os seguintes: alterarNome, depósito e saque; no construtor, saldo é opcional,
# com valor default zero e os demais atributos são obrigatórios.


class ContaCorrente:
    def __init__(self, numero_conta: int, nome_correntista: str, saldo: decimal = 0.0):
        self._numero_conta = self.valida_numero_conta(numero_conta)
        self._nome_correntista = self.valida_nome(nome_correntista)
        self._saldo = self.valida_saldo(saldo)

    @staticmethod
    def valida_nome(nome_correntista: str) -> str:
        if not isinstance(nome_correntista, str):
            raise ValueError('Nome do correntista deve ser uma string')
        return nome_correntista

    @staticmethod
    def valida_saldo(saldo: decimal) -> decimal:
        if not isinstance(saldo, (int, float, decimal)):
            raise ValueError('Saldo deve ser um número decimal')
        return saldo

    @staticmethod
    def valida_numero_conta(numero_conta: int) -> int:
        if not isinstance(numero_conta, int):
            raise ValueError('Número da conta deve ser um número inteiro')
        return numero_conta

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def nome_correntista(self):
        return self._nome_correntista

    @property
    def saldo(self):
        return self._saldo

    @numero_conta.setter
    def numero_conta(self, numero_conta: int):
        self._numero_conta = self.valida_numero_conta(numero_conta)  # Acesse

    @nome_correntista.setter
    def nome_correntista(self, nome_correntista: str):
        self._nome_correntista = self.valida_nome(nome_correntista)  # Acesse _nome_correntista

    @saldo.setter
    def saldo(self, saldo: decimal):
        self._saldo = self.valida_saldo(saldo)  # Acesse _saldo diretamente

    def alterarNumeroConta(self, numero_conta: int):
        self._numero_conta = self.valida_numero_conta(numero_conta)  # Acesse _numero_conta

    def alterarSaldo(self, saldo: decimal):
        self._saldo = self.valida_saldo(saldo)  # Acesse _saldo diretamente

    def alterarNome(self, nome_correntista: str):
        self._nome_correntista = self.valida_nome(nome_correntista)  # Acesse _nome_correntista

    def deposito(self, valor: decimal):
        self._saldo = self.valida_saldo(valor + self._saldo)  # Acesse _saldo diretamente

    def saque(self, valor: decimal):
        if self._saldo >= valor:
            self._saldo = self.valida_saldo(self._saldo - valor)  # Acesse _saldo diretamente
        else:
            print('Saldo insuficiente')

    def __str__(self):
        return (f'Conta Corrente\n'
                f'Número da conta: {self.numero_conta}\n'
                f'Nome do correntista: {self.nome_correntista}\n'
                f'Saldo: {self.saldo}')


if __name__ == '__main__':
    conta = ContaCorrente(123, 'João', 100.0)
    print(conta)
    conta.deposito(50.0)
    print(conta)
    conta.saque(20.0)
    print(conta)
    conta.saque(100.0)
    print(conta)
    conta.alterarNome('Maria')
    print(conta)
    conta.alterarNumeroConta(456)
    print(conta)
    conta.alterarSaldo(200.0)
    print(conta)
    conta.deposito(50.0)
    print(conta)
    conta.saque(100)
