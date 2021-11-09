# 4. Посчитать сумму числового ряда от 0 до 14 включительно. Например, 0+1+2+3+…+14

print("4. Посчитать сумму числового ряда от 0 до 14 включительно. Например, 0+1+2+3+…+14")
number_1 = 1
number_2 = 14
print("number 1 = 1")
print("number 2 = 14")
sumOfNumbers = sum(list(range(number_1, number_2 + 1)))

print(f"sum of numbers form {number_1} to {number_2} is: ", sumOfNumbers)
