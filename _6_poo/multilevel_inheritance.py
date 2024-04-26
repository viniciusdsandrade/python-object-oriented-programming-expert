class Organism:
    alive = True


class Animal(Organism):
    @staticmethod
    def eat():
        print('This animal is eating')

    @staticmethod
    def sleep():
        print('This animal is sleeping')


class Dog(Animal):
    @staticmethod
    def bark():
        print('This dog is barking')


class SheperdDog(Dog):
    @staticmethod
    def protect():
        print('This dog is protecting')


dog = SheperdDog()
dog.alive = True
dog.eat()
dog.sleep()
dog.bark()
dog.protect()
