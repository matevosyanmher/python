# 1. Write a function to multiply all the numbers in a given list
def multiply(lists):
    result = 1
    for i in lists:
        result = result * i
    return result


lists = [1, 2, 3, 4]

print(multiply(lists))
