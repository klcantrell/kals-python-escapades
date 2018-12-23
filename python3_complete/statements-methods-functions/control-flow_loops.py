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

# useful operators

# range
print('using range')
for num in range(3, 10):  # third arg is step size
    print(num)

# enumerate
# without
index_count = 0
my_word = 'abcde'
for letter in my_word:
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1
# with
print('with enumerate')
for index, letter in enumerate(my_word):
    print('At index {} the letter is {}'.format(index, letter))

# zip
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300, 400]  # zip stops at shortest list

for item in zip(mylist1, mylist2):
    print(item)
print('list cast zip of arrays', list(zip(mylist1, mylist2, mylist3)))

# in operator
dict_for_in_example = {'mykey': 345}
print('x' in ['x', 'y', 'z'])
print('mykey' in dict_for_in_example)
print(345 in dict_for_in_example.values())

# min and max
list_with_numbers = [59, 12, 1, 4]
print(min(list_with_numbers))
print(max(list_with_numbers))

# random
from random import shuffle, randint
ordered_list = [1, 2, 3, 4, 5, 6]
shuffle(ordered_list)
print(ordered_list)
print(randint(0, 20))

# user input
result = input('Enter a number: ')
print(result)