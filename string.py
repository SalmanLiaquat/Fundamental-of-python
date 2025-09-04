# string take extra space because every string has unique code

a ='A'
print(ord(a)) # ASCII value: 65

# ord -> convert unicode into integer
# chr -> convert integer into unicode
a=65
print(chr(a))

 # string Indexing

language ='python'
print(language[0]) # output: p
print(language[-1]) # output: n


# string slicing

language ='python'
print(language[0:2]) # output: py
print(language[:-1]) # output: pytho

# Question i have to get sher as output  

a='sher Ali'
print(a[0:4:1]) # start:End:steps

# string and type conversion 

# Explicit conversion :by using type casting str(),f;oat(),int(),bool() 

age=23
age =str(age)
print(type(age))

# Falsy value(7) : 0,false,""(empty string),[],{},()


# Implicit conversion : automatically convert one data type to another

age =46/2
print(type(age))



# Raw and formatted string

name = 'salman'
age= 23
study ='The University of lahore'

print('Hello! My name is ',name,' and my age is ',age,'I am studying at',study)

# formatted string
print(f'Hello! My name is {name} and my age is {age}. I am studying at {study}')

# raw string: print string as it is (\ treat it as a literal character instead of eascaping it)
print(r'Hello! My name is \n salman and my age is \n 23. I am studying at The University of lahore')


#input and output 
# for output we use print() function
# for input we use input() function


number =int(input('Enter your Age: '))
print(type(number))


# Task Question 

# 1. Accept number from the user
#2. Accept age from the user and print it
number = int(input('Enter your number: '))
myAge = int(input("Enter your Age That is: "))
print (f'Your age is {myAge}')