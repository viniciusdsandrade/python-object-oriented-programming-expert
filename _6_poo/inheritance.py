class Animal:
    alive = True

    @staticmethod
    def eat():
        print('This animal is eating')

    @staticmethod
    def sleep():
        print('This animal is sleeping')


class Dog(Animal):
    @staticmethod
    def run():
        print('This dog is running')


class Fish(Animal):
    @staticmethod
    def swim():
        print('This fish is swimming')


class Bird(Animal):
    @staticmethod
    def fly():
        print('This bird is flying')


bird = Bird()
dog = Dog()
fish = Fish()

# metódos presentes na classe Animal
bird.eat()
bird.sleep()
dog.eat()
dog.sleep()
fish.eat()
fish.sleep()

# metódos presentes na classe Bird
bird.fly()

# metódos presentes na classe Dog
dog.run()

# metódos presentes na classe Fish
fish.swim()
