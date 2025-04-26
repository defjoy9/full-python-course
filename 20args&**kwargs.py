# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
#             * unpacking operator
#             1. positional 2. default 3. KEYWORD 4. arbitrary



def add(x,y):
    return x + y


print(add(1,2))


def add(*args):
    total  = 0
    for arg in args:
        total +=arg
    return total


print(add(1,2,3,4,5))


def add(*nums):
    total  = 0
    for num in nums:
        total +=num
    return total


print(add(1,2,3,4,5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")


print(display_name("duh","dr.","yuh"))

# --------------------------------------------------------------------------------

def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print(print_address(street="213 fake street",
                    apt="1000",
                    city="detroit",
                    state="MI",
                    zip="54321"))



def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


shipping_label("Dr.","spongebob","squarepants","III",
               street="Fake street 123",
            #    apt="#100",
               city="detroit",
               state="MI",
               zip="54321")

shipping_label("Dr.","spongebob","squarepants","III",
               street="Fake street 123",
               apt="#100",
               city="detroit",
               state="MI",
               zip="54321")

shipping_label("Dr.","spongebob","squarepants","III",
               street="Fake street 123",
               pobox="PO box #100",
               city="detroit",
               state="MI",
               zip="54321")