# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop


numbers = [1,2,3,4,5]


for number in reversed(numbers):
    print(number, end=" ")

numbers = (1,2,3,4,5)

for item in numbers:
    print(item)

fruits = {"apple","orange","banana","coconut"}

for fruit in fruits:
    print(fruit)


name = "def joy"

for character in name:
    print(character, end=" ")


my_dictionary = {
    "A": 1,
    "B": 2,
    "C": 3
}

#only keys
for key in my_dictionary:
    print(key)

#only values
for value in my_dictionary.values():
    print(value)

#both keys and items
for key, value in my_dictionary.items():
    print(key, value)