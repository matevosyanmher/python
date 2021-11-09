# 3. Вывести на экран все чётные значения в диапазоне от 1 до 497;
# solution 1
print("3. Вывести на экран все чётные значения в диапазоне от 1 до 497;")

numRange = list(range(1, 498))

for i in numRange:
    if i % 2 != 0:
        numRange.remove(i)

print(numRange)

# solution 2
i = 0
while i < 496:
    i = i + 2
    print(i, end=" ")
print()
