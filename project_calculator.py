# project 2

print("What would you like to do:\n1. Addition\n2. Substract\n3. Divide\n4. Multiply")
option = input("(type in a number)\n>")

x = float(input("Enter value of first number: "))
y = float(input("Enter value of second number: "))

if option == "1":
    result = x + y
    print(f"{x} + {y} = {round(result, 3)}")
elif option == "2":
    result = x - y
    print(f"{x} - {y} = {round(result, 3)}")
elif option == "3":
    result = x / y
    print(f"{x} / {y} = {round(result, 3)}")
elif option == "4":
    result = x * y
    print(f"{x} * {y} = {round(result, 3)}")
else:
    print("Please type in a number")
