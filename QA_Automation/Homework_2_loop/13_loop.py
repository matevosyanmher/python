# 13. Calculate the cube of all numbers from 1 to a given number from user
print("13. Calculate the cube of all numbers from 1 to a given number from user")

special_characters = "!@#$%^&*()-+?_=,<>/"
userInput = input("Please input number: ")

while userInput.isalpha() or userInput in special_characters:
    userInput = input("Input is not numeric, please input number: ")
userInput = eval(userInput)

for i in range(userInput + 1):
    print(f"Cub for {i} : = ", i ** 3)
