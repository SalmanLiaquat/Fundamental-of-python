# Condition: allow to make decision by execute different block of code based on the condition
# if-else
#if
#if-elif-else

# task 1:
'''
a =15 
if a>10:
    print(f"Task A is assigned")
else:
    print(f"Task B is Assigned")


#task 2


while True:
 print(f'8 . To exit the program')
 print(f'1 . To continue the program')
 option =int(input("Enter the option: "))

 if option ==8:
    print(f"✅ Thanks for using. Goodbye!")
    break
 if option ==1:
  money =int(input("Enter the Amount that mother give you to buy chocolate: "))
 

  if money<10:
    print(f"I need more money")
    break
  elif money ==10:
    print(f'In {money} rupees only I can buy chocobar')
  elif money==20:
    print(f'In {money} rupees i will buy mango icecream')
  else:
    print(f'In {money} rupees i will buy cone icecream')


'''

# Some Question related to conditional statement


# q1: Accept two number and tell the greater number
'''
n1=int(input("Enter 1st Number:"))
n2=int(input("Enter 2nd Number:"))
if n1>n2:
    print(f"{n1} is greater then {n2}")
elif n1==n2:
    print(f"{n1} is equal to {n2}")
else:
    print(f"{n2} is greater then {n1}")

'''

# q2: Accept the gendar from the user as a char and message good morning sir(on the basis of gender)
'''
gender = input("Enter For Male (M) and For Female (F):")

if gender =='M' or gender == 'm':
    print ("Good Morning Sir")
elif gender =='F' or gender == 'f':
    print(f"Good Morning Madam")
else:
    print("You are not male and female")

'''

#q3: Accept the Integer and tell it even or odd

'''
number =int(input('Enter the Number:- '))
if number %2 ==0:
    print(f"{number} is Even Number")
else:
    print(f"{number} is Odd Number")

'''

#q4: Accept the nme and age from the user and tell him he i s a  eligible for not
'''
name =input("Enter Your Name:")
age =int(input("Enter Your Age:"))
if age >=18:
    print(f"{name}, You are eligible to vote because you are {age} years old.")
else:
    print(f"{name}, you are not eligible because of under 18 years")

'''

#q5:Accept a year and check if it is leap year or not
#leap year: divisible by 4 and not divisible by 100 center year:(2000,3000) divisible by 400
'''
year =int(input("Enter the Year:"))

if year %100==0 and year%400 ==0:
    print(f"{year} is a leap year")
elif year %4==0 and year%100 !=0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

'''

#Q5 temperature check

temp =int(input("Enter the temperature:"))

if temp < 0:
    print("Freezing Weather")
elif temp in range(0,10):
    print("Very Cold Weather")
elif temp in range(10,20):
    print("Cold Weather")
elif temp in range(20,30):
    print("Pleasent Weather")
elif temp in range(30,40):
    print("hot Weather")
else:
    print("Boiling Weather")