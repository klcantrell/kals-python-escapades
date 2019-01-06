# intro to passing functions around


def hello(name='Kal'):
    private_var = 'private info'

    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet function inside hello'

    def welcome():
        return '\t This is the welcome function inside hello and I have access to {info}'.format(info=private_var)

    print("I'm going to return a function")

    if name == 'Kal':
        return greet
    else:
        return welcome


salutation = hello('Cloud')


def run_callback(cb):
    print('Running callback')
    cb()


run_callback(lambda: print(salutation()))

# decorators


def my_decorator(original_function):
    def wrap_function():
        print('Some extra code, before the original function')
        original_function()
        print('Some extra code, after the original function')
    return wrap_function


# this would be equal to my_decorator(function_with_decorator)()
@my_decorator
def function_with_decorator():
    print('I want to be decorated')


function_with_decorator()
