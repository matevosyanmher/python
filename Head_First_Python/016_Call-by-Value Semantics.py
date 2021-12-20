def double(arg):
    print("Argument before: ", arg)
    arg = arg * 2
    print("Argument after is: ", arg)


def change(arg):
    print("before argument: ", arg)
    arg.append("more data")
    print("After: ", arg)


#
num = 10
double(num)
print(num)

saying = 'Hello '
double(saying)
print(saying)
numbers = [42, 256, 16]
double(numbers)
print(numbers)

change(numbers)
print(numbers)
