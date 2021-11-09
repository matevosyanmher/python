# 12. Reverse a given integer number
print("12. Reverse a given integer number")

numberToRevers = eval(input("Please input number you want to reverse: "))
revers = 0
reminder = 0

while numberToRevers != 0:
    reminder = numberToRevers % 10
    revers = revers * 10 + reminder
    numberToRevers = numberToRevers // 10

print(revers)
