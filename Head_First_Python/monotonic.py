lst = [1, 2, 3, 9, 5, 6]


# This is the same as the previous example, but with a generator
def gen_func():
    for i in range(len(lst) - 1):
        if lst[i] <= lst[i + 1]:
            yield "ok"
        else:
            yield "not"


# This is the same as the previous example, but with a generator
def gen_func2():
    for i in range(len(lst) - 1):
        if lst[i] <= lst[i + 1]:
            yield "ok"
        else:
            yield "not"


def is_monotonic(lst):
    new = []
    for i in range(len(lst) - 1):
        if lst[i] <= lst[i + 1]:
            new.append("ok")
        else:
            new.append("not")
    nset = set(new)
    if len(nset) > 1:
        print("False")
    else:
        print("True")


is_monotonic(lst=lst)
print(list(gen_func()))
