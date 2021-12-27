class Person:
    NUMBER_OF_COPIES = 0

    def __init__(self, name, surname, place_of_birth):
        self.name = name
        self.surname = surname
        self.place_of_birth = place_of_birth

        Person.NUMBER_OF_COPIES += 1

    def print_info(self):
        print(f'Name: {self.name}, Surname: {self.surname}, Place of birth: {self.place_of_birth}')

    def __hash__(self) -> int:
        return super().__hash__()


p1 = Person('Ilon', 'Musk', 'ՀԱՀ')
p1.print_info()
p2 = Person('Mher', 'Matevosyan', 'Vanadzor')
p2.print_info()
print(Person.NUMBER_OF_COPIES)


class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area(self, radius):
        return Circle.PI * radius ** 2

    def get_length(self, radius):
        return Circle.PI * 2 * radius


c1 = Circle(5)
print(c1.get_length(5))