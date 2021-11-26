# 1. Write a function to multiply all the numbers in a given list
def multiply(lst):
    result = 1
    for i in lst:
        result = result * i
    return result


lists = [1, 2, 3, 4]

print(multiply(lists))
