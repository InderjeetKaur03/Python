# if, Elif, Else statement

 if (1==1):
  # do something
 elif (1==3):
  # do something
 else:
  # do something

# for loop
for i in iterable_item:
 print(i)

# While
while(value==true):
 # do something
else:
 # do something

# break, continue, pass

# range() for iteration
for num in range(3, 10): # but not including 10
 print(num)

# enumerate
index_count = 0
word ='abcde'
for letter in word:
  print(word[index_count])
  index_count +=1

for item in enumerate(word):
 print(item)

'x' in [1,2,4] # in keyword
# min and max functions for lists
# import a library

from random import shuffle
mylist = [1,2,3,4,5,6,9,7]
shuffle(mylist)

# list comprehensions
mylist = [num for num in range(0,10)]
mylist = [num**2 for num in range(0,10)]
mylist = [num for num in range(0,10) if num%2==0]



 

