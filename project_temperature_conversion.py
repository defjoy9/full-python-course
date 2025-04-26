# project 4

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temparature: "))

if unit == "C":
    tempt = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}")
else:
    print(f"{unit} is an invalid unit of measurement")