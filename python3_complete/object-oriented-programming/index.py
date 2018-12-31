# class basics


class Dog():
    # class object attribute
    # same for any instance
    species = 'mammal'

    # "constructor"
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # methods
    def bark(self, number):
        print('WOOF! ' * number +
              'My name is {name}'.format(name=self.name))


my_dog = Dog(breed='Lab', name='Dudley')
my_dog.bark(3)


class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_circumference(self):
        return self.radius * Circle.pi * 2


my_circle = Circle()
print(my_circle.get_circumference())
