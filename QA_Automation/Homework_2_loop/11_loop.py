# 11. Find the factorial of a given number
print("11. Find the factorial of a given number")

special_characters = "!@#$%^&*()-+?_=,<>/ "
n = input("Please enter positive integer number: ")
while n.isalpha() or n in special_characters or eval(n) <= 0:
    n = input("Invalid input, please enter positive integer number: ")
n = eval(n)
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f"The factorial of {n} is : ", fact)
