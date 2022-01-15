


def concat(*args):
    return [a for arg in args for a in arg]

print(concat([1, 2, 3], [4, 5], [6, 7]) )

print(concat([1], [2], [3], [4], [5], [6], [7]) )

print(concat([1, 2], [3, 4]))

print(concat([4, 4, 4, 4, 4]) )

