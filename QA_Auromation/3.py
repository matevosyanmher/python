import random

# 03. Write a program to remove duplicates from a list
print("03. Write a program to remove duplicates from a list")

salmpleList_3 = ["apple", "orange", "lemon", "apple"]

# noDublicateList = set(salmpleList_3) # version 1

noDublicateList =  []

for item in salmpleList_3:              #version 2
    if item in noDublicateList:
        continue
    else:
        noDublicateList.append(item)
        
