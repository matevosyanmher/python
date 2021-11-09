# 6. Используя цикл while, выведите на экран для числа 2 его степени от 0 до 20.
print("6. Используя цикл while, выведите на экран для числа 2 его степени от 0 до 20.")
i = 0
while i <= 20:
    print(2 ** i)
    i += 1

# 7. Print the following pattern
print("7. Print the pattern ")

# declaring the list

patternList = [5, 4, 3, 2, 1]
print(patternList)  # printing tne firs row
for i in range(5, 1, -1):  # printing other rows
    patternList.remove(i)
    print(patternList)
print()
