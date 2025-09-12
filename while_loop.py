#Q : print the digit one by one in separate line

'''
num =256
while num > 0:
    print(num%10)
    num //=10
'''

#Q: take input and print it in rverseorder
'''
num =int(input("Enter the number:"))
rev =0
while num>0:
    rev = rev*10 + num%10
    num //=10

print(rev)
'''

# Q CHECK THE NUMBER IS PALINDROME OR NOT
'''
num =int(input("Enter the number:"))
temp=num
rev =0
while num>0:
    rev = rev*10 + num%10
    num //=10
if  rev== temp:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

'''

# Q create a number guessing game and tell the total tries

import random
number = random.randint(1,10)
tries =0
while True:
  
    guess =int(input("Enter the number:"))
    if guess == number:
        print("You got it")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")
    tries +=1

print(f"You total tries: {tries} ")