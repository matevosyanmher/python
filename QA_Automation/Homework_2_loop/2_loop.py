import random

# 2. Calculate the sum of all numbers from 1 to a given number from user
print("2. Calculate the sum of all numbers from 1 to a given number from user")

start = 1
special_characters = "!@#$%^&*()-+?_=,<>/"
userInput = input("Please input number: ")

while userInput.isalpha() or userInput in special_characters:
    userInput = input("Input is not numeric, please input number: ")

# a = str(sum(range(1, 6)))
# print(a)
print(f"Sum of numbers from 1 to {userInput} is: ", str(sum(range(start, int(userInput) + 1))))

# 2. Дано три числа. Найти количество положительных чисел среди них

print("2. Дано три числа. Найти количество положительных чисел среди них")

x_1 = random.randint(-100, 100)
x_2 = random.randint(-100, 100)
x_3 = random.randint(-100, 100)

counter = 0
numList = [x_1, x_2, x_3]

for i in numList:
    if i > 0:
        counter += 1
    # else:
    #     continue
print(f"First number is: {x_1}")
print(f"Second number is: {x_2}")
print(f"Third number is: {x_3}")
print("The count of positive numbers is:", counter)
