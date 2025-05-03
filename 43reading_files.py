# Python reading files (.txt, .json, .csv)

# read .txt
file_path = "files/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You do not have permission to read that file")

# read JSON
import json

file_path = "files/output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        print(content["age"])
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You do not have permission to read that file")

# read CSV
import csv

file_path = "files/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
            print(line[1])
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You do not have permission to read that file")