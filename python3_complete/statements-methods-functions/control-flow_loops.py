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

# while loops

x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('x is not less than 5')

array_2 = [1, 2, 3]
for item in array_2:
    pass
print('end of loop through array_2')
name = 'Sammy'
for letter in name:
    if letter == 'a':
        continue
    print(letter)
for num in array_2:
    if (num == 2):
        print('breaking out of iterating through array_2')
        break
    print(num)