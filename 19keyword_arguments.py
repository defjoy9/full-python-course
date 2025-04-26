# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary



def hello(greeting,title,first,last):
    print(f"{greeting} {title}{first} {last}")


hello("Hello", "Mrs.", "Duh", "Yuh")
hello("Hello", last="Yuh",first="Duh", title="Mrs.")


for i in range(1,11):
    print(i, end=" ")

print("1","2","3","4","5", sep="-") # 1-2-3-4-5

def get_phone(country,area, first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)