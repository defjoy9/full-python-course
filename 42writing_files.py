# Python writing files (.txt, .json, .csv)

txt_data = "I like pizza"
file_path = "files/output.txt" #relative



# with will close the file for you
# write
with open(file=file_path, mode="w") as file:
    file.write(txt_data)
    print(f"txt file {file_path} was created")

#exclusive creation
try:
    # with will close the file for you
    with open(file=file_path, mode="x") as file:
        file.write("\n" + txt_data)
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("That file already exists!")

# append
try:
    with open(file=file_path, mode="a") as file:
        file.write(txt_data)
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("That file already exists!")

employees = ["Eugene", "Squidward", "Spongebob","Patrick"]
try:
    with open(file=file_path, mode="w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("That file already exists!")

# JSON FILE
import json

file_path = "files/output.json"

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

try:
    with open(file=file_path, mode="w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file {file_path} was created")
except FileExistsError:
    print("That file already exists!")

# CSV FILE
import csv

file_path = "files/output.csv"

employees = [["Name","Age","Job"],
            ["Spongebob",30,"Cook"],
            ["Patrick",37,"Unemployed"],
            ["Sandy",27,"Scientist"]]


try:
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file {file_path} was created")
except FileExistsError:
    print("That file already exists!")
