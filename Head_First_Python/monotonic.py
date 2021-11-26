lst = [1, 2, 3, 4, 5, 6]


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


is_monotonic(lst)
