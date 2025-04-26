# collection = single "variable" used to store multiple values
# List  = [] ordered and changable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# list
fruits = ["apple","orange","banana","coconut"]

print(dir(fruits))
print(help(fruits))
print(fruits[0])
print(len(fruits))
print("apple" in fruits)

fruits[0] = "pineapple"
fruits.append("apple")
fruits.remove("pineapple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("apple"))
print(fruits.count("banana"))

print(fruits[0:3]) #print 3 elements
print(fruits[:3]) # print 3 elements
print(fruits[::2]) # print every second element
print(fruits[::-1]) # reverse

for fruit in fruits:
    print(fruit)


# set
fruits = {"apple","orange","banana","coconut"}

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapplle" in fruits)

fruits.add("pineapple")
fruits.remove("pineapple")
fruits.pop()
fruits.clear()

# tuple

fruits = ("apple","orange","banana","coconut")

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapplle" in fruits)

print(fruits.index("apple"))
print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit)
