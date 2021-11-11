# 01. Write a program to sum all the items in a list
sampleList_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("sum of items of the list is: ", sum(sampleList_1))

# 02. Write a program to get the largest number from a list
sampleList_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Max value of the list is: ", max(sampleList_2))

# 03. Write a program to remove duplicates from a list
print("03. Write a program to remove duplicates from a list")

salmpleList_3 = ["apple", "orange", "lemon", "apple"]

# noDublicateList = set(salmpleList_3) # version 1

noDublicateList = []

for item in salmpleList_3:  # version 2
    if item in noDublicateList:
        continue
    else:
        noDublicateList.append(item)

# 04. Write a program to check a list is empty or not
print("04. Write a program to check a list is empty or not")

salmpleList_4 = ["apple", "orange", "lemon", "apple"]

if len(salmpleList_4) > 0:
    print("List is not empty")
else:
    print("List is empty")

# 05. Write a program to copy a list
print("05. Write a program to copy a list")

salmpleList_5 = ["apple", "orange", "lemon", "apple"]
copedList = []
copedList.extend(salmpleList_5)
print(copedList)

# 06. Write a Python program to create a list with infinite elements
salmpleList_6 = []
element = "aaa"
while True:
    salmpleList_6.append(element)

# 07. Write a Python program to convert a string to a list

salmpleList_7 = []
str = "Es im anush Hayastani arevaham barn em sirum"
salmpleList_7.extend(str.split(" "))
print(salmpleList_7)

# 08. Write a Python program to insert a given string at the beginning of all items in a list
sampleList_8 = [1, 2, 3, 4]
string = "emp"

for i in range(len(sampleList_8)):
    sampleList_8[i] = string + str(sampleList_8[i])
print(sampleList_8)

# 09. Write a Python program to find the item with maximum occurrences in a given lisy
salmpleList_9 = ["apple", "orange", "lemon", "apple", "apple", "banana"]
print(max(salmpleList_9, key=salmpleList_9.count))

# 10. Write a Python program to check whether a specified list is sorted or not
sampleList_10 = [1, 2, 4, 6, 8, 10, 12, 14, -16, 17]

# for i in range(len(sampleList_10) - 1):
if all(sampleList_10[i] <= sampleList_10[i + 1] for i in range(len(sampleList_10) - 1)):
    print("ok")
else:
    print("not")

