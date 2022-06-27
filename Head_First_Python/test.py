'''creat class person with private fields name and age'''


class Person1:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # def get_name(self):
    #     return self.__name
    #
    # def get_age(self):
    #     return self.__age

    def __str__(self):
        return "Name: " + self.__name + " Age: " + str(self.__age)


class Student(Person1):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def __str__(self):
        return super().__str__() + " Grade: " + str(self.__grade)


samson = Student("Samson", 18, "A")
print(samson)
