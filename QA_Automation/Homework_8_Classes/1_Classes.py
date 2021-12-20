import pprint
# 1.  Write a class named Student with two attributes student_id, student_name. Add a new attribute student_class.
#     Create a function to display the entire attribute and their values in Student class.
class Student:
    def __init__(self, student_id: int, student_name: str, student_class: int = 1):
        self.student_id = student_id
        self.student_name = student_name
    def set_class(self, student_class: int):
        self.student_class = student_class
    def get_student_class(self):
        return self.student_class
    def __str__(self):
        return "Student_id is %s, student_name is %s and student_class is %s" % (
            self.student_id, self.student_name, self.get_student_class())
student1 = Student(student_id=5, student_class=10, student_name="Mher")
student1.set_class(10)
print(student1.__str__())
# 2. Create a Vehicle class without any variables and methods
class Vehicle:
    pass
# 3. Write a program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self, max_speed: int, mileage: int):
        self.max_speed = max_speed
        self.mileage = mileage
carVehicle = Vehicle(max_speed=100, mileage=200000)
print(f"Car max speed is {carVehicle.max_speed} and mileage is {carVehicle.mileage}")
# 4. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    pass
carBus = Bus(max_speed=250, mileage=230000)
print(f"Bus mileage is {carBus.mileage} and max speed is {carBus.max_speed}")
''' 5. Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a
default value of 50.'''
class Bus1(Vehicle):
    def __init__(self, max_speed: int, mileage: int, capacity: int = 50):
        super().__init__(max_speed, mileage)
        self.capacity = capacity
carBus1 = Bus1(max_speed=150, mileage=178000, capacity=80)
print(f"Bus1 max speed is {carBus1.max_speed}, mileage is {carBus1.mileage} and capacity is {carBus1.capacity}")
