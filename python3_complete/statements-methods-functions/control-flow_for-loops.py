# control flow statements

hungry = False

if hungry:
    print('FEED ME')
else:
    print('NO FOOD PLEASE')

loc = 'Auto Shop'

if loc == 'Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool!')
else:
    print('I do not know much')

# for loops
my_numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in my_numbers_list:
    if number % 2 == 0:
        print(f'Even number: {number}')
    else:
        print(f'Odd number: {number}')
for letter in 'Hello string':
    print(letter)
my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
for a, b in my_list:
    print('tuple unpacking item a', a)
    print('tuple unpacking item b', b)
my_dict = {'k1': 1, 'k2': 2, 'k3': 3}
for key, value in my_dict.items():
    print(f'value is {value} for key {key}')
