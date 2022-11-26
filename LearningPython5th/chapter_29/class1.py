class Supper():
    def hello(self):
        self.data1 = 'spam'


class Sub(Supper):
    def hola(self):
        self.data2 = 'eggs'


X = Sub()
print(X.__dict__)
print(X.__class__)
print(Sub.__base__)
print(Supper.__base__)

Y = Sub()

X.hello()
print(X.__dict__)
X.hola()
print(X.__dict__)

print(list(Sub.__dict__.keys()))
print(list(Supper.__dict__.keys()))

print(Y.__dict__)

print(X.data1)
print(X.__dict__['data1'])

X.data3 = 'toast'
print(X.__dict__)
X.__dict__['data3'] = 'ham'
print(X.data3)
print(dir(X))
