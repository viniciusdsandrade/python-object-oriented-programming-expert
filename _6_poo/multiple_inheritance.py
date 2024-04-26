class Prey:
    @staticmethod
    def flee():
        print("This animal is fleeing.")


class Predator:
    @staticmethod
    def hunt():
        print("This animal is hunting.")


class Mouse(Prey):

    @staticmethod
    def flee():
        print("The mouse is fleeing.")


class Cat(Predator, Prey):

    @staticmethod
    def flee():
        print("The Cat is fleeing.")

    @staticmethod
    def hunt():
        print("The Cat is hunting.")


class Dog(Predator):

    @staticmethod
    def hunt():
        print("The Dog is hunting.")


mouse = Mouse()
cat = Cat()
dog = Dog()

mouse.flee()

cat.flee()
cat.hunt()

dog.hunt()
