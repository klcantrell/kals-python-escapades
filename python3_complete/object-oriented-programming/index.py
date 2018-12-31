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

# inheritance


class Animal():

    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


my_animal = Animal()
my_animal.who_am_i()


class Canine(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def who_am_i(self):
        print('I am a dog')

    def bark(self):
        print('WOOF!')


my_canine = Canine()
my_canine.who_am_i()
my_canine.bark()

# polymorphism


class Baby():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says "gaga"'


class Adult():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says "hello"'


my_baby = Baby('Maddox')
my_adult = Adult('Kalalau')

print(my_baby.speak())
print(my_adult.speak())


def polymorphic_loop():
    for human in [my_baby, my_adult]:
        print(type(human))
        print(human.speak())


polymorphic_loop()


def human_speak(human):
    print(human.speak())


human_speak(my_baby)
human_speak(my_adult)

# abstract class


class Human():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError(
            'Subclass must implement this abstract method')


# my_human = Human('Jordan')
# my_human.speak()  # raises an error

class LittleHuman(Human):

    def __init__(self, name):  # exploring the __init__ method
        Human.__init__(self, name)
        print('Little Human created')

    def speak(self):
        return self.name + ' says "gaga"'


class BigHuman(Human):

    def speak(self):
        return self.name + ' says "Hello"'


my_little_human = LittleHuman('Little Maddox')
print(my_little_human.speak())

my_big_human = BigHuman('Dada')
print(my_big_human.speak())
