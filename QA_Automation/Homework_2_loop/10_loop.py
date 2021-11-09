# 10. Display Fibonacci series up to 10 terms
print("10. Display Fibonacci series up to 10 terms")
special_characters = "!@#$%^&*()-+?_=,<>/ "
a, b = 0, 1
n = input("How many terms do you want: ")
while n.isalpha() or n in special_characters or eval(n) < 0:
    n = input("Invalid input, please enter positive integer number: ")
n = eval(n)
if n == 0:
    print(" ")
elif n == 1:
    print(a)

else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)
