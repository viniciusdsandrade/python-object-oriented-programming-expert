import math


# Questão 1

# Escreva uma classe cujos objetos representam alunos matriculados em uma disciplina. Cada objeto
# dessa classe deve guardar os seguintes dados do aluno:

# matrícula,
# nome,
# 2 notas de prova e
# 1 nota de trabalho.

# Escreva os seguintes métodos para esta classe:

# media calcula a média final do aluno (cada prova tem peso 2,5 e o trabalho tem peso 2)
# final calcula quanto o aluno precisa para a prova final (retorna zero se ele não for para a final)


class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, trabalho):
        if not isinstance(matricula, int):
            raise TypeError('Matrícula deve ser um número inteiro')

        if not isinstance(nome, str):
            raise TypeError('Nome deve ser uma string')

        if ((not isinstance(nota1, (int, float))) or
                (not isinstance(nota2, (int, float))) or
                (not isinstance(trabalho, (int, float)))):
            raise TypeError('As notas devem ser números inteiros ou decimais')

        if not 0 <= nota1 <= 10 or not 0 <= nota2 <= 10 or not 0 <= trabalho <= 10:
            raise ValueError('As notas devem ser entre 0 e 10')

        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.trabalho = trabalho

    def media(self):
        return math.ceil((self.nota1 + self.nota2) * 2.5 + self.trabalho * 2) / 7

    def final(self):
        media = self.media()
        if media >= 7:
            return 0
        elif 5 <= media < 7:
            return 10 - media
        else:
            return 'Reprovado'

    def __eq__(self, other):
        return self.matricula == other.matricula

    def __hash__(self):
        return hash(self.matricula)

    def __str__(self):
        return (f'Aluno:        {self.nome}\n'
                f'Matrícula:    {self.matricula}\n'
                f'Nota 1:       {self.nota1}\n'
                f'Nota 2:       {self.nota2}\n'
                f'NotaTrabalho: {self.trabalho}\n'
                f'Média:        {round(self.media(), 3)}\n'
                f'Nota p/ final: {round(self.final(), 3) if isinstance(self.final(), (int, float)) else self.final()}')


aluno1 = Aluno(1, 'João', 7, 8, 9)
aluno2 = Aluno(2, 'Maria', 5, 6, 7)
aluno3 = Aluno()

print(aluno1)
print()
print(aluno2)
