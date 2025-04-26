# function = A block of reusable code
#            place () after the functions name to invoke it

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to {name}!")


happy_birthday("duh", 20)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")


display_invoice("duh9",49.10, "01/09")


# return = statement used to end a function
#          and send a result back to the caller

print()

def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x *y
    return z

def divide(x,y):
    z = x /y
    return z

print(add(1,2))
print(substract(1,2))
print(multiply(1,2))
print(divide(1,2))


def create_name(firstname, lastname):
    firstname = firstname.capitalize()
    lastname = lastname.capitalize()
    return firstname + " " + lastname


full_name = create_name("duh", "yuh")

print(full_name)