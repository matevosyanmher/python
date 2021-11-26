# 10. Write a Python program to check whether a specified list is sorted or not
sampleList_10 = [1, 2, 4, 6, 8, 10, 12, 14]

# for i in range(len(sampleList_10) - 1):
if all(sampleList_10[i] <= sampleList_10[i + 1] for i in range(len(sampleList_10) - 1)):
    print("ok")
else:
    print("not")
