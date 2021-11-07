# 4. Write a program to convert a tuple of string values to a tuple of integer values. Go to the editor
originalTuple = ('333', '33', '1416', '55')
lst = list(originalTuple)
# [int(x) for x in lst]
for x in range(len(lst)):
    lst[x] = int(lst[x])

originalTuple = tuple(lst)
print(originalTuple)
