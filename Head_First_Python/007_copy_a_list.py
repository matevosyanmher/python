first = [1, 2, 3, 4, 5, 6, 7, 8, 9]
second = first
print(first)
print(second)
first.append(33)
print(first)
print(second)
third = second.copy()
third.append(99)
print(second)
print(third)
