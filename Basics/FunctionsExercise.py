def myfunc():
    print('Hello World')

def myfunc(a):
    if a == True:
        return 'Hello'
    elif a == False:
        return 'Goodbye'

def myfunc(x,y,z):
    if z==True:
        return x
    elif z==False:
        return y

def myfunc(num1,num2):
    return num1+num2

def is_even(a):
    value = False
    if a%2==0:
        value=True
    return value
     
def is_greater(a,b):
    if a>b:
        return True
    else:
        return False

def myfunc(*args):
 return sum(args)

def myfunc(*args):
 mylist =[]
 for i in args:
  if i%2==0:
      mylist.append(i)
 return mylist

def myfunc(myInput):
    myOutput=''
    for index, value in enumerate(myInput):
        if(index%2==0):
            myOutput+=value.upper()
        else:
            myOutput+=value.lower()
    return myOutput

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers 
# if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        if a>b:
            return b
        else:
            return a            
    elif (a%2!=0 or b%2!=0):
        if a>b:
            return a
        else:
            return b 


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    a,b = text.split()
    if a[0].lower()==b[0].lower():
        return True
    else:
        return False

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1,n2):
    if n1==20 or n2==20 or n1+n2==20:
        return True
    else:
        return False

# Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    a, b = name[0:3], name[3:]
    return a.capitalize()+ b.capitalize()

# Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    return " ".join(text.split()[::-1])

# Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    if 90<=n<=110 or 190<=n<=210:
     return True
    else:
     return False

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):
    for i,n in enumerate(nums):
        if i<len(nums)-1 and nums[i] == nums[i+1]:
            return True
    return False 

'''
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''
def paper_doll(text):
    rStr = ''
    for c in text:
        rStr += c*3
    return rStr   

'''
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
'''

def blackjack(a,b,c):
    if (a+b+c)<=21:
        return (a+b+c)
    elif (a==11 or b==11 or c==11) and (a+b+c)-10<21:
        return (a+b+c)-10
    else:
        return 'BUST'

'''
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
'''
def summer_69(arr):
    if 6 not in arr:
        return sum(arr)
    else:        
        index_of_6 = arr.index(6)        
        index_of_9 = arr.index(9)        
        a = sum(arr[0:index_of_6])
        if index_of_9<=len(arr)-1:
         return a+sum(arr[index_of_9+1:])
        return a

'''
Write a Python function that checks whether a word or phrase is palindrome or not.
'''
def palindrome(s):
    if s==s[::-1]:
     return True
    else:
     return False

'''
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
'''

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    check = "".join(str1.lower()).replace(' ','')
    for c in alphabet:
        if c in check:
            alphabet= alphabet.replace(c,'')
    if len(alphabet) ==0:
        return True
    else:
        return False

'''
Check 007 pattern in given list, numbers need not be adjacent
'''

def spy_game(nums):
   check = [0,0,7,'a']
   for n in nums:
       if n==check[0]:
           check.pop(0)
   print(len(check)==1)
       
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])

# Count primes : ignore 0 and 1

def count_primes(num):
    # check for 1 and 2
    if num<2:
        return 0
       
    primes = [3] # Creating list of prime numbers   
    x=3 # Conuter for numbers to check upto given numbers
    
    while x<=num: # iterating through all numbers upto numbers
      for y in range(3,x,2): # check if number is prime
         if x%y==0:
             x=x+2
             break
      else:
          primes.append(x)
          x=x+2
    print(primes)
    return len(primes)
    
    
count_primes(100)
