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
my_other_list = [0] * 3
print('my_other_list', my_other_list)

# dictionaries

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup['apple'])
prices_lookup['bread'] = 3.75
prices_lookup['apple'] = 3.20
print(prices_lookup)
print('dict keys', prices_lookup.keys())
print('dict values', prices_lookup.values())
print('dict items', prices_lookup.items())

# tuples

t = (1, 2, 3, 3)
l = [1, 2, 3]
print(type(t))
print(type(l))
print(t[-2])
print('typle count method', t.count(3))
print('typle index method', t.index(3))
# t[0] = '1' # does not support item reassignment

# sets

myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(2)
print(myset) # no dupes
lists_with_dupes = [1,1,1,2,2,3,4,5,6,6,6]
print(set(lists_with_dupes)) # removes dupes

# booleans

print(type(True))
print(type(False))
print(1 > 2)
placeholder_b = None

# file input and output

myfile = open('test.txt')
myfile_contents = myfile.read()
print(myfile_contents)
myfile.seek(0)
print(myfile.readlines())
myfile.close()
myfile_absolutepath = open('/Users/jordan/Desktop/dev/kals-python-escapades/python3_complete/basics/test.txt')
print('absolute path readlines', myfile_absolutepath.readlines())
myfile_absolutepath.close()
with open('test.txt', mode='r') as myfile_usingwith:
  contents = myfile_usingwith.readlines()
  print('myfile using "with"', contents)
with open('fileToBeOverwritten.txt', mode='a') as f:
  f.write('/NFOURONFOURTH')
with open('oiuasodiuoasduoia.txt', mode='w') as f:
  f.write('I CREATED THIS FILE')
with open('oiuasodiuoasduoia.txt', mode='r') as f:
  print(f.read())

  # comparison & logical operators

print('2 == 2', 2 == 2)
print('"2" == 2', '2' == 2)
print ('1 < 2', 1 < 2)
print('1 != "1"', 1 != '1')
print('1 < 2 and 2 < 3', 1 < 2 and 2 < 3)
print('1 > 2 and 2 < 3', 1 > 2 or 2 < 3)
print('not 1 == 1', not 1 == 1)