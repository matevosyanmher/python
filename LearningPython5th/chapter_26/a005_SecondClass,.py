from a004_TheFirstExample import FirstClass


class SecondClass(FirstClass):

    def display(self):
        print('Current value = "%s"' % self.data)


FirstClass.newVar = "Hello"

a = SecondClass()
a.setdata('42')
a.display()

x = FirstClass()
x.setdata('100')
x.display()

z = SecondClass()
z.newVar = "newVar333"
print(z.newVar)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):
        self.data *= other


a = ThirdClass('abc')
a.display()
print(a)
b = a + 'xyz'
print(b)
b.mul(3)
print(b)
dat = b.data
print(list(dat))
print(ThirdClass.__bases__)
