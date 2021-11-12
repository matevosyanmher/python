# 1. Write a program to read first n lines of a file
print("1. Write a program to read first n lines of a file")

file = open("file_name.txt", "r")

for i in range(1, 4):
    line = file.readline()
    print(line)
