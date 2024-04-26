class Car:
    wheel = 4  # variavel de classe

    def __init__(self, make, model, year, color):
        self.make = make  # variavel de instancia
        self.model = model  # variavel de instancia
        self.year = year  # variavel de instancia
        self.color = color  # variavel de instancia


car1 = Car('Ford', 'Fiesta', 2019, 'Red')
car2 = Car('Chevrolet', 'Onix', 2020, 'Black')

car1.wheel = 3  # alterando a variavel de classe para o objeto car1

print(car1.wheel)  # 3
print(car2.wheel)  # 4
print(Car.wheel)  # 4
