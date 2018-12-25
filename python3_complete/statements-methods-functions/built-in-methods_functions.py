# exploring built-in methods

mylist = [1, 2, 3]

mylist.append(4)
print(mylist)

mylist.pop()
print(mylist)

mylist.insert(0, 2)
print(mylist)

# functions


def send_to_console(content):
    print(content)


def send_hello_to_output(output_stream, content='Hello'):  # defaykt paraneters
    '''
    Sends content to output
    '''
    output_stream(content)


send_hello_to_output(send_to_console)


def say_hello(name='NAME'):
    return f'Hello {name}'


greeting = say_hello('Cloud')
print(greeting)


def add(n1, n2):
    return n1 + n2


add_result = add(1, 2)
print(add_result)


def dog_check(s):
    return 'dog' in s.lower()


print(dog_check('My dog is awesome'))


def pig_latin(word):
    first_letter = word[0]
    if first_letter.lower() in 'aeiou':
        return word + 'ay'
    else:
        return word[1:] + first_letter + 'ay'


print(pig_latin('Apple'))

# *args and *kwargs


def sum_func(*args):  # pass in as many args.  gets turned into tuple.
    return sum(args) * 0.5


print(sum_func(1, 2, 3, 4, 5))


def func_for_kwargs(**kwargs):  # kwargs is dict of parameters and values
    if 'fruit' in kwargs:
        print('My favorite fruit is {}'.format(kwargs['fruit']))
    else:
        print('No fruit here')


func_for_kwargs(fruit='Banana')


def args_and_kwargs(*args, **kwargs):  # order matters and can't mix
    print('args are', args)
    print('kwargs are', kwargs)
    print('I would like {arg} {kwarg}'.format(
        arg=args[0], kwarg=kwargs['food']))


args_and_kwargs(10, 20, 30, fruit='orange', food='eggs')
