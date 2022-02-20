class Person:
    __NUMBER_OF_COPIES = 0

    def __init__(self, name, surname, place_of_birth):
        self.__name = name
        self.surname = surname
        self.place_of_birth = place_of_birth
        Person.__NUMBER_OF_COPIES += 1

    @property
    def name(self):
        return self.__name

    # @classmethod
    # def get_name(cls):
    #     return cls.__name


class Student(Person):
    def __init__(self, name, surname, place_of_birth, year_of_birth, grade):
        super().__init__(name, surname, place_of_birth)
        self.year_of_birth = year_of_birth
        self.grade = grade

    def get_name(self):
        return self.name


student1 = Student("Marvin", "Miller", "Henchmen", 1995, "A")
print(student1.get_name())

#
#
#
# class Circle:
#     PI = 3.14
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return Circle.PI * self.radius ** 2
#
#     def get_length(self):
#         return round(2 * Circle.PI * self.radius, 2)
#
#
# class NewCircle(Circle):
#     def __init__(self, radius: int) -> None:
#         super().__init__(radius)
#
#
# c2 = NewCircle(radius=5)
# print(c2.get_area())
# print(c2.get_length())
