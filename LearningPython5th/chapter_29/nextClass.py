class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)


x = NextClass()
x.printer('instance call')
print(x.message)


class Supper:
    def method(self):
        print('In Supper method')


class Sub(Supper):
    def method(self):
        print('starting Sub.method')
        Supper.method(self)
        print('end Sub.method')


print()
a = Sub()
a.method()
