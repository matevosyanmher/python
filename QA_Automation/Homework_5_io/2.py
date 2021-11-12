# 2. Write a program to find the longest words
file = open("file_name.txt", "r")

lst = list(file)
newList = []
for i in lst:
    a = i.strip("\n")
    newList.append(a)
print(max(newList, key=len))


