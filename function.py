# FUNCTION: Block of code that will execute only when it is called 
'''
def greet():
    print(f"Hello! This is the python course beginning.")

greet()
'''

# ARGUMENT ANDF PARAMETER
'''
#POSITIONAL ARGUMENT

def sum(a,b):     #parameter: the value you accept
    return a+b

result = sum(2,5)    #argement: the value you provide
print(f"The sum of two values is: {result}")

'''

# KEYWORD ARGUMENT

'''
def area(radius):
    return 3.14 *pow(radius,2)

print(f"The area of circle is: {area(radius=5)}")
'''
'''
def info(name,age):
    print(f"Your Name is {name} and age is {age}")

info(name= "salman" , age = 23)
'''

# DEFAULT ARGUMENT\
'''
def authentication(role ="Guest"):
    print(f"{role} is Working")

authentication() # default value show on output
authentication("Admin") # argument value should be consider

'''

#Q to check the  string is palindromw or not

'''
def palindrome(name):
    rev =""
    for char in name:
        rev = char + rev
    
    if rev == name:
        print(f"{name} is palindrom")
    else:
        print(f"{name} is not palindrom")


palindrome("madam")
palindrome("python")
'''


# VARIABLE WITH MULTIPLE NUMBER OF ARGUMENT
# 1.*args → multiple positional arguments
# 2.**kwargs → multiple keyword arguments

#1
'''
def add_all(*num):
    add=0
    for n in num:
        add+=n
    return add

print(add_all(1,2,3,4,5))

'''
#2
'''
def info (**data):
    for key,value in data.items():
        print(f"{key}: {value}")
info(name="Salman Liaquat",id =70132579,age=23)
'''




#lambda Function (Anonymous Function)
#Lambda = one-line short function.
'''
multiple =lambda x,y:x*y
print(multiple(2,3))

'''

# Recursion: Function call itself
'''
def factorial(num):
    if num ==0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))

'''

# Built-in-function
# map() → apply function to all elements
#  filter() → filter elements
# reduce() → reduce to single value


#MAP()
'''
num =[1,2,3,4,5]

square =list(map(lambda x:x*x,num))

print(square)

'''

#FILTER

'''
num = [1, 2, 3, 4, 5]



even =filter(lambda x: x%2 == 0,num)

print(list(even))
'''

# REDUCE
from functools import reduce
num = [1, 2, 3, 4, 5]

total =reduce(
    lambda x,y:x+y,
    num
)

print(total)