'''
n= int(input("Enter the number :-"))

try:
    print(10/n)
except Exception as err:
    print("Error:",err)
else:
    print("Succesffully you execute the code")
finally:
    print("I am always execute")

'''


age = int(input("Enter your age:-"))

try:
    if age>=18:
        print("You are eligible to vote")
    else:
        raise ValueError("You are below 18 and you are not eligible to vote")

except ValueError as err:
    print("Error:",err)
