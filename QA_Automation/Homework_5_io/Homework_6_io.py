# 1. Write a program to read first n lines of a file
print("1. Write a program to read first n lines of a file")

file = open("file_name.txt", "r")

for i in range(1, 4):
    line = file.readline()
    print(line)

# 2. Write a program to find the longest words
file = open("file_name.txt", "r")

lst = list(file)
newList = []
for i in lst:
    a = i.strip("\n")
    newList.append(a)
print(max(newList, key=len))

# 3. Write a Python program to copy the contents of a file to another file
with open("file_name.txt", "r") as firstFile, open("write_file.txt", "a") as secondFile:
    for line in firstFile:
        secondFile.write(line)

# 4. Write a program to read a random line from a file. use "import random" for generating random number
import random

lineNumber = random.randint(0, 3)
print(lineNumber)

with open("file_name.txt", "r") as f:
    line = f.readlines()[lineNumber]
    print(line)

# 5. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string
import os

if not os.path.exists("letters"):
    os.makedirs("letters")
letter = string.ascii_uppercase
for letter in string.ascii_uppercase:
    with open("C:\\Users\Mher\PycharmProjects\python\QA_Automation\Homework_6_io\letters\\" + letter + ".txt", "w") as f:
        f.write(letter)
        f.close



