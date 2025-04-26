
name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

result = len(name) # length of a string
result = name.find(" ") # First occurance if it can't find it return -1
result = name.rfind("o") # Last occurance
result = name.capitalize() # First letter capitalize
result = name.upper() # All letters are upper case
result = name.lower() # All letters are lower case
result = name.isdigit() # If only digits
result = name.isalpha() # Boolean, only alphabetical letters 
result = phone_number.count("-") # how many '-' characters are in the string
result = phone_number.replace("-", " ") # replace character
#print(help(str)) # lists string methods

#print(result)


# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("username is longer than 12 characters")
elif username.find(" ") != -1:
    print("username must not contain spaces")
elif not username.isdigit():
    print("username must not contain any digits")
# elif not username.isalpha():
#     print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")