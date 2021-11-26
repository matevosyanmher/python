# 5. Write a Python function that takes a number as a parameter and check the number is prime or not
def prime(k):
    if k == 1:
        return False
    elif (k == 2):
        return True
    else:
        for x in range(2, k):
            if k % x == 0:
                return False
        return True


print(prime(7))
