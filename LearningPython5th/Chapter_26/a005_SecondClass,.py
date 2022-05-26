from a004_TheFirstExample import FirstClass


class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)


FirstClass.newVar = "Hello"

z = SecondClass()

a = SecondClass()
a.setdata('42')
a.display()

x = FirstClass()
x.setdata('100')
x.display()
