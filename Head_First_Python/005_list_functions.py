print("# Remove")
lstToRemove = [1, 2, 3, 4, 5, 6]
lstToRemove.remove(2)
print(lstToRemove)

print("# Pop")
lstToPop = [1, 2, 3, 4, 5, 6, 7, 8, 9]
popedObject = lstToPop.pop()
print(popedObject)
print(lstToPop)

print("# Extend")
lstToExtend = [2]
lstToExtend.extend([3, 4])
print(lstToExtend)
lstToExtend.append([4, 5])
print(lstToExtend)
lstToExtend.extend([6, 7])
print(lstToExtend)
print("# Insert")
lstToInsetrt = [2, 3, 4]
lstToInsetrt.insert(0,1)
print(lstToInsetrt)
help(list.insert)

