def fib(iteracia):
    a = 0
    b = 1
    for i in range(iteracia):
        c = a + b
        a = b
        b = c
    return c


print(fib(20))
