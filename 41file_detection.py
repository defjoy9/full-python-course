# Python file detection
import os

file_path = "files/test.txt" # relative file path
file_path = "/home/kali/projects/python/fullcourse/files/test.txt" # absolute file path
file_path2 = "files/"


if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")