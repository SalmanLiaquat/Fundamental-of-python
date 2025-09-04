# Arithmetic Operators: (+, -, *, /, %, //, **)
# Mini Calculator Project

print("----- Calculator Functionalities -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Floor Division")
print("7. Exponent")
print("8. Exit")

while True:
    option = int(input("\nSelect an option (1-8): "))

    if option == 8:
        print("✅ Thanks for using the calculator. Goodbye!")
        break
    if option<1 or option>8:
        print("❌ Invalid Input. Please select from 1–8.")
        continue

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    match option:
        case 1:
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        case 2:
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        case 3:
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        case 4:
            if num2 != 0:
                print(f"Result: {num1} ÷ {num2} = {num1 / num2}")
            else:
                print("❌ Error: Division by zero is not allowed.")
        case 5:
            if num2 != 0:
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            else:
                print("❌ Error: Modulus by zero is not allowed.")
        case 6:
            if num2 != 0:
                print(f"Result: {num1} // {num2} = {num1 // num2}")
            else:
                print("❌ Error: Floor division by zero is not allowed.")
        case 7:
            print(f"Result: {num1} ^ {num2} = {num1 ** num2}")



# Assignment Operators: (+=, -=, *=, /=, %=, //=, **=)


a=20
#a+=a
#print(a)
a+=40
print(a)
a+=60
print(a)


# Comparison operators: (==, !=, >, <, >=, <=)
#logical operators: (and, or, not)

# given task handle both operators 

age =int(input('Enter your age: '))

if age>=18 and age<=30:
    print("you are in matureage")
elif age<18 and age>10:
    print("you are in teenage")
elif age<=10 and age>0:
    print("you are in childhood")
else:
    print("you are in senior age")


