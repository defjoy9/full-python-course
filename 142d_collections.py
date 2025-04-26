
fruits = ["apple","orange","banana","coconut"]
vegentables =["celery","carrots","potatoes"]
meats = ["chicken","fish","turkey"]

groceries = [fruits, vegentables, meats]
groceries = [["apple","orange","banana","coconut"], 
             ["celery","carrots","potatoes"], 
             ["chicken","fish","turkey"]] 
# second way of declaring a 2D list

fruits[0] = "pinapple"
print(fruits)

print(groceries[0]) # row, fruits
print(groceries[1]) # row, vegetables
print(groceries[2]) # row, meats

print(groceries[0][1]) # orange in fruits



for collection in groceries:
    #print(collection)
    for food in collection:
        print(food, end=" ")
    print()

# exercise
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()