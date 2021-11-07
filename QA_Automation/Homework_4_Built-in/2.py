# 2. Write a program to get the top three items in a shop. Go to the editor
sampleData = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

dictValues = sampleData.values()
someList = list(dictValues)
someList.sort()
print(someList[-3:])