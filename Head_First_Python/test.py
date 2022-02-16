'''creat class person with name and age'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Person: " + self.name + " " + str(self.age)


class Student(Person):
    def __init__(self, name, age, major):
        Person.__init__(self, name, age)
        self.major = major

    def __str__(self):
        return "Student: " + self.name + " " + str(self.age) + " " + self.major


st1 = Student("John", 20, "Math")
print(st1)
