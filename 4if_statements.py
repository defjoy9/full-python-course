# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up")

response = input("would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you")

name = input("Enter your name: ")
if name == "":
    print(f"Hello {name}")
else:
    print("You haven't typed a name!")

online = True

if online:
    print("The user is online")
else:
    print("The user is offline")
