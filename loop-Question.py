# question 1: Accept integer from input and print hello wold in time


n= int(input("Enter the number to print n time `hello!world`: "))
for i in range(1,n+1,1):
    print("Hello!World")



# question 2: Print Natural Number to n times

n=int(input("Enter the number: "))

for i in range (1,n+1):
    print(i)



# Question 3: Sum up to n terms

n=int(input("Enter the number: "))
sum = 0
for i in range(1,n+1):
   sum += i

print(sum)
   


# Question 4: Accrpt a number and check is it is a perfect number or not
# whose sum of factors is equal to iself a number and is called perfect number

n = int(input("Enter the number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print(f"{n} is a perfect number ")
else:
    print(f"{n} is not a perfect number ")



#Question 5: Factorial of the number


n = int(input("Enter the number: "))
fact = 1

for i in range(1,n+1):
    fact *= i

print(f"The factorial of {n} is {fact}")



#Question 5: print sum of all even and odd number in range

n = int(input("Enter the number: "))
even_sum=0
odd_sum=0

for i  in range(1,n+1):
    if i%2 == 0:
        even_sum +=i
    else:
        odd_sum +=i
print(f"The Even_sum: {even_sum}")
print(f"The odd_sum: {odd_sum}")



#Question 6: print all the factor of the number

n = int(input("Enter the number: "))
for i in range(1,n+1):
    if n%i ==0:
     print(i)



# Question 7 check weather the number is prime or not
# {2,3,5,7,11...}


n = int(input("Enter the number: "))

if n<=1:
    print("It is not a prime number")
else:
    for i in range(2,n):
        if n % i ==0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")




num = int(input("Enter the number: "))
if num<2:
    print("It is not a prime number")
else:
 for i in range(2,num):
    if num<2:
        continue
    for j in range(2,i):
        if i%j ==0:
            break
    else:
        print(i)  #output:2,3,5,7



# Question8: Reverse the string


name =input("Enter the name:")
for i in range(len(name),0,-1):
    print(name[i-1],end="")



#Question 9 : count alphabet, digit, special charters in the string

st = "2324str@#$"
alpha=0
digit = 0
special_charater=0

for i in st:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    else:
        special_charater += 1
print(f"Alphabet: {alpha}")
print(f"Digit: {digit}")
print(f"Special Charater: {special_charater}")

# Question 10: Find the same (repeated) numbers in the string
'''
number = '232434565'
count = 1

for i in range(len(number)):
    for j in range(i+1,len(number)):
        if number[i] == number[j]:
            print(number[i],end=" ")
            break

<<<<<<< HEAD
           
=======

            
'''


#Print A in loop
#  

n=5
for i in range(1, n + 1):
    # spaces before stars
    for j in range(n - i):
        print(" ", end="")
    # stars and inner spaces
    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2 or i==3:  # first or last star
            print("*", end="")
        else:
            print(" ", end="")
    print()
>>>>>>> dcbf888 (Add loop-question file)
