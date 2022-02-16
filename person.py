class Person:
    NUMBER_OF_COPIES = 0

    def __init__(self, name, surname, place_of_birth):
        self.__name = name
        self.surname = surname
        self.place_of_birth = place_of_birth

        Person.NUMBER_OF_COPIES += 1

    def __repr__(self):
        return print(f"{self.__name}, {self.surname}, {self.place_of_birth}")

    def __hash__(self) -> int:
        return super().__hash__()


p1 = Person('Elon', 'Musk', 'ՀԱՀ')
p1.__repr__()
p2 = Person('Mher', 'Matevosyan', 'Vanadzor')
p2.__repr__()
print(Person.NUMBER_OF_COPIES)


class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return Circle.PI * self.radius ** 2

    def get_length(self):
        return Circle.PI * 2 * self.radius


class NewCircle(Circle):
    def __init__(self, radius: int) -> None:
        super().__init__(radius)


c2 = NewCircle(radius=6)
c2.get_length()
print(c2.get_area())
