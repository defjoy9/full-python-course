# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates


capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Ukraine": "Kyiv"
}
# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem() # remove latest key inswerted
#capitals.clear()

keys = capitals.keys()

for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)

for value in capitals.values():
    print(value)


items = capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")