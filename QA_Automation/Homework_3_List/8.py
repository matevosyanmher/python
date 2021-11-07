# 08. Write a Python program to insert a given string at the beginning of all items in a list
sampleList_8 = [1, 2, 3, 4]
string = "emp"

for i in range(len(sampleList_8)):
    sampleList_8[i] = string + str(sampleList_8[i])
print(sampleList_8)