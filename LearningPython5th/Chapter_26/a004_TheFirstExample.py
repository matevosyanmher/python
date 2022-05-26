class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


if __name__ == "__main__":
    x = FirstClass()
    y = FirstClass()
    x.setdata("King Arthur")
    y.setdata(3.14159)
    x.display()
    y.display()

    x.data = "New value"
    x.display()
    x.setdata(y.data)
    x.display()
    x.another_name = "spam"
    print(x.another_name)
