# user input ⌨️ input() = A function that prompts the user to enter data
#              Returns the entered data as a string


name = input("What is your name?: ")
age = int(input("How old are you?: "))

print(f"Hello {name}!\n You are {age} years old")

age = age + 1

print(f"A year from now you will be {age}")

# Exercise 1 Rectangle Area Calc

length = float(input("Length: "))
width = float(input("Width: "))

area = length * width
print(area)

# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?:")
price = float(input("What is the price?:"))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s\n Your total is ${price}")