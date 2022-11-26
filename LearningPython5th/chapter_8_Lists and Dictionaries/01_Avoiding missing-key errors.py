Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99

if (2, 3, 4) in Matrix:
    print(Matrix[(2, 3, 4)])
else:
    print(0)

print(Matrix.get((2, 3, 49), 0))

D = dict(name='bob', age=45)
print(D)
D = dict(zip(('one', 'two', 'three'), (1, 2)))
print(D)
