import math

friends = 0
# friends = friends + 1
friends += friends
friends -= 2
friends *= 3
friends /= 2
friends **= 2
remainder = friends % 3

x = 3.14
y = -4
z = 5
v = 9

result = round(x)
result = abs(y)
result = pow(4, 3)
result = max(x, y, z)
result = min(x, y, z)

print(math.pi)
print(math.e)
result = math.sqrt(v)
result = math.ceil(x)
result = math.floor(x)

# Exercise 1

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}")

# Exercise 2

radious = float(input("Enter a radius of a circle: "))
area = math.pii * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm^2")

# Exercise 3

a = float(input("Enter side A:"))
b = float(input("Enter side B:"))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")