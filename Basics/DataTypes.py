# String operations

name="Inderjeet Kaur"
arn ="arn:aws:iam:123456789:user/inder"
print("Split function" + " "+arn.split("/")[1])
print("Upper Case : " + name.upper())
print("Upper Case : " + name.lower())
print("Length function : ", len(name))
print("Replace : " + name.replace("jeet","jit"))
print(name.split())

# .format method

print('This is a {}'.format('string'))
print('This is {2} {0} {1}'.format('my', 'new', 'string'))
print('This is {a} {b} {c}'.format(a='my', b='new', c='string'))

# decimal precision

value = 100/436563
print('My decimal value : {r = 1.3f}'.format(r=value)

# f strings - > formatted literal strings

var= "world"
print(f"Hello {var}")

# Lists

my_list = [1,2,3,4,5,6]
my_list.append(7)
my_list.pop()
my_list.pop(4)
my_list.sort()
my_list.reverse()

# Distionaries

my_dict = {'key1': 'value1', 'key2': 'value2' }
print(my_dict['key1'])
my_dict.keys()
my_dict.values()
my_dict.itemss()

# Tuples - immutable
t = (1,2,4)

# bool values -> true, false

# Sets - unordered collection of unique elements

myset = {1,3,4,5,6}

# I/O with files , create myfile.txt, should be your working directory

# works only in Jupyter

%%writefile myfile.txt
Hello, this is a text file
myfile = open('myfile.txt')
myfile = read()
myfile.seek(0)
myfile.close()
with open('myfile.txt', mode ='r') as my_file: # you dont need to explicitly close the file at the ned your task

  contect = my_file.read()

# Comparison operators -> ==, <=, >=, <, >, !=

# chaining of operators : and , or , not

