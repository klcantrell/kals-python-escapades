# ======
print('Straight function')


def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


for x in create_cubes(10):
    print(x)


# ======
print('Generator')


def create_cubes_gen(n):
    for x in range(n):
        yield x**3


for x in create_cubes_gen(10):
    print(x)


# ======
print('Fibonacci with generators')


def gen_fib(n):
    a = 1
    b = 1

    for _i in range(n):
        yield a
        a, b = b, a + b


for number in gen_fib(10):
    print(number)

# ======
print('Fibonacci with straight function...less memory efficient')


def gen_fib_straight(n):
    a = 1
    b = 1
    output = []

    for _i in range(n):
        output.append(a)
        a, b = b, a + b


for number in gen_fib(10):
    print(number)


# ======
print('simple generator')


def simple_gen():
    for x in range(3):
        yield x


g = simple_gen()

print(next(g))
print(next(g))
print(next(g))
try:
    print(next(g))
except StopIteration:
    print("Nothing left to call next on!")


# ======
print('Create an iterator')
my_string = 'Kal'
my_iterator = iter(my_string)
print(next(my_iterator))
