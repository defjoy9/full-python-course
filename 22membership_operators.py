# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in


word = "APPLE"

letter = input("guess a letter in a secret word: ")
# STRING
if letter in word:
    print(f"there is a {letter}")
else:
    print(f"{letter} was not found")
# reversed
if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"there is a {letter}")

# SETS 
students = {"Spongebob","Patrick","Sandy"}

student = input("enter the name of the student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")
#reversed
if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")

#DICTIONARY

grades = {"Sandy":"A",
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}

student = input("enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

# ---------

email = "fakemail@gmail.com"

if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")