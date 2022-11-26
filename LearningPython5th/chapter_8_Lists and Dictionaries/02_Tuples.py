T = (1, 2, 3, ['a', 'b', 'c'], 'kkk',)
print(T[3][0])
T[3][0] = 7
print(T)
print(len(T))
T = tuple('spam')
print(T)
print(T * 2)
T = T + T
print(T)
print('s' in T)
print(T.index('s'))
print(T.count('s'))
T = ('cc', 'aa', 'dd', 'bb')
print(sorted(T))

from collections import namedtuple

Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
bob = Rec('Bob', 18, ['dev', 'mgr'])
print(bob)
