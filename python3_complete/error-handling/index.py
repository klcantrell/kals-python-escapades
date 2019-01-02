def add(n1, n2):
    return n1 + n2


# number1 = 10
# number2 = input('Please provide a number: ')

# try:
#     result = add(10, number2)
# except:
#     print('Something is up with number2...casting it to an integar')
#     number2 = int(number2)
#     result = add(10, number2)
#     print(result)
# else:
#     print(result)
# finally:
#     print('This will run no matter what')

try:
    f = open('testfile.txt', 'r')
    f.write('Writing a test line')
except TypeError:
    print('There was a type error!')
except OSError as e:
    print('There was an OS error! {}'.format(e))
except:
    print('All other exceptions!')
finally:
    print('This will run no matter what')


def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print("Whoops!  That's not a number")
            continue
        else:
            print('Yes, thank you. {n} is a number'.format(n=result))
            break
        finally:
            print('End of try/except/finally')

ask_for_int()