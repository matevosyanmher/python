"""
Record and process information about people.
Run this file directly to test its classes.
"""
import formats
from classtools import AttrDisplay  # Use generic display tool


class Person(AttrDisplay):  # Mixin a repr at this level
    """
    Create and process person records
    """

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):  # assume last name is last word in name
        return self.name.split()[-1]

    def giveRise(self, percent):
        self.pay = int(self.pay * (1 + percent))  # percent must be 0...1

    # def __repr__(self):
    #     return '[Person: %s, %s]' % (self.name, formats.money(self.pay, 10))


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)  # job name is implied

    def giveRise(self, percent, bonus=0.1):
        Person.giveRise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100_000)
    print(bob)
    print(sue)
    sue.giveRise(0.1)
    print(sue)
    # print('{0:.2f}'.format(sue.pay, ','))
    # print(formats.money(sue.pay, 10, 'AMD '))
    tom = Manager('Tom Jones', 60_000)
    print(tom)
    tom.giveRise(.2)
    print(tom)
    print()
    print(bob.__class__.__name__)
    print(tom.__class__.__name__)
    print(tom.__class__.__bases__)
    print(tom.__class__.__mro__)
    print(tom.__dict__.keys())
    print(tom.__dict__.values())
    # for key in tom.__dict__.keys():
    #     print(key, '=>', tom.__dict__[key])

    for key in tom.__dict__.keys():
        print(key, '=>', getattr(tom, key))

    print(getattr(tom, 'aaa', 'sssssss'))
