class Employee:
    i = 10
    # make a private class variable
    __private_var = 'private'

    @classmethod
    def set__private_var(cls, value):
        cls.__private_var = value

    @classmethod
    def get_private_var(cls):
        return cls.__private_var

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # make a private method
    def __str__(self):
        return self.name

    def fullname(self):
        self.name = self.first + ' ' + self.last

    def compute_salary(self):
        return format(self.pay * 6, ",") + " this is from class Employee"

    def give_raise(self):
        pass

    def promote(self):
        pass

    def retire(self):
        pass


class Engineer(Employee):
    def __init__(self, first, last, pay, department):
        super().__init__(first, last, pay)
        self.department = department

    def compute_salary(self):
        return format(self.pay * 12, ",") + " \"this is from class Engineer\""


bob = Employee('Bob', 'Smith', 50000)
sue = Employee('Sue', 'Jones', 60000)
tom = Engineer('Tom', 'Smith', 50000, 'IT')

print(bob.compute_salary())
print(sue.compute_salary())
print(tom.compute_salary())
print()
company = [bob, sue, tom]
for emp in company:
    print(emp.compute_salary())

a = Employee.i
print(a)
b = Engineer.i
print(b)

print(bob.__dict__)
print(sue.i ** 2)
print(Employee.__dict__)
# print(Employee.name) # AttributeError: type object 'Employee' has no attribute 'name'
bob.fullname()
print(bob.name)
Employee.set__private_var('public')
print(bob.get_private_var())
