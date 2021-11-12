# 4. Write a program to read a random line from a file. use "import random" for generating random number
import random

lineNumber = random.randint(0, 3)
print(lineNumber)

with open("file_name.txt", "r") as f:
    line = f.readlines()[lineNumber]
    print(line)
