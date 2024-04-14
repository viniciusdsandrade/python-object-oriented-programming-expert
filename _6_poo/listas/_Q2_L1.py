# Questão 2
# Escreva uma classe Data cuja instância (objeto) represente uma data. Esta classe deverá dispor dos
# seguintes métodos:
# 1 - construtor:  define a data que determinado objeto (através de parâmetro), este método verifica se a
#       data está correta, caso não esteja a data é configurada como 01/01/0001
# 2 - compara: recebe como parâmetro um outro objeto da Classe data, compare com a data corrente e
# retorne:
#   0  se as datas forem iguais;
#   1  se a data corrente for maior que a do parâmetro;
#  -1  se a data do parâmetro for maior que a corrente.
# 3 - getDia retorna o dia da data
# 4 - getMes retorna o mês da data
# 5 - getMesExtenso retorna o mês da data corrente por extenso
# 6 - getAno retorna o ano da data
# 7 - isBissexto retorna verdadeiro se o ano da data corrente for bissexto e falso caso contrário
# 8 - clone o objeto clona a si próprio, para isto, ele cria um novo objeto da classe Data com os
#     mesmos valores de atributos e retorna sua referência pelo método

class Date:
    def __init__(self, day, month, year):

        if not isinstance(day, int):
            raise TypeError('Dia deve ser um número inteiro')

        if not isinstance(month, int):
            raise TypeError('Mês deve ser um número inteiro')

        if not isinstance(year, int):
            raise TypeError('Ano deve ser um número inteiro')

        if not Date.is_valid_date(day, month, year):
            raise ValueError('Data inválida')

        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_valid_date(day, month, year):
        if day < 1 or day > 31: return False
        if month < 1 or month > 12: return False
        if year == 0: return False
        if year == 1582 and month == 10 and day > 4: return False
        if month in [4, 6, 9, 11] and day > 30: return False
        if month == 2 and day > 29: return False
        return month != 2 or day <= 28 or Date.is_bissexto(year)

    @staticmethod
    def is_bissexto(year):
        if year % 4 != 0: return False
        elif year % 100 != 0: return True
        elif year % 400 != 0: return False
        else: return True

    def get_week_day_name(self):
        day = self.day
        month = self.month
        year = self.year

        if month == 1 or month == 2:
            month += 12
            year -= 1

        k = year % 100
        j = year // 100

        day_of_week = (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

        days = ['Sábado', 'Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']

        return days[day_of_week]

    def get_month_name(self):
        months = ['Janeiro', 'Fevereiro', 'Março',
                  'Abril', 'Maio', 'Junho', 'Julho',
                  'Agosto', 'Setembro', 'Outubro',
                  'Novembro', 'Dezembro']
        return months[self.month - 1]

    def get_day(self): return self.day

    def get_month(self): return self.month

    def get_year(self): return self.year

    def get_difference_between_two_dates(self, other):
        if self.compare(other) == 0:
            return 0
        if self.compare(other) == 1:
            return self.get_difference_between_two_dates(other.clone())
        else:
            days = 0
            while self.compare(other) == -1:
                other.day -= 1
                days += 1
                if other.day == 0:
                    other.month -= 1
                    if other.month == 0:
                        other.year -= 1
                        other.month = 12
                    other.day = 31 if other.month in [1, 3, 5, 7, 8, 10, 12] else 30
                    if other.month == 2:
                        other.day = 29 if other.is_bissexto(other.year) else 28
            return days

    def clone(self):
        return Date(self.day, self.month, self.year)

    def compare(self, other):
        if self.year > other.year:
            return 1
        elif self.year < other.year:
            return -1
        else:
            if self.month > other.month:
                return 1
            elif self.month < other.month:
                return -1
            else:
                if self.day > other.day:
                    return 1
                elif self.day < other.day:
                    return -1
                else:
                    return 0

    def __eq__(self, other):
        return (self.day == other.day and
                self.month == other.month and
                self.year == other.year)

    def __hash__(self):
        return hash((self.day, self.month, self.year))

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'


date1 = Date(6, 12, 2001)
date2 = Date(14, 4, 2024)

print(date1.get_difference_between_two_dates(date2))
print(date1.get_week_day_name())
print(date1.get_month_name())
