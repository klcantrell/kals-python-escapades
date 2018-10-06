# variables and numbers

my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)

# string properties

name = 'Sam'
last_letters = name[1:]
print('P' + last_letters)
x = 'Hello World'
print(x.upper())
print(x.lower())
print(x.split())

# string interpolation

print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 100 / 77
print('The result was {:1.3f}'.format(result))

name = "Jose"
print(f'Hello, his name is {name}')
name = "Sam"
age = 3
print(f'Hello, {name} is {age} years old')

# lists

my_list = [1, 2, 3]
my_list.append(7)
popped_item = my_list.pop()
other_popped_item = my_list.pop(0)
print('popped item', popped_item)
print('other popped item', other_popped_item)
print('original list (mutated)', my_list)
letters_list = ['a', 'e', 'i', 'z', 'b']
num_list = [4, 87, 1, 5, 7, 8]
letters_list.sort()
print('sorted list in place', letters_list)
num_list.reverse()
print('num list reversed (mutated)', num_list)
