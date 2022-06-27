from person import Person


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRise(self, percent, bonus=0.1):
        self.person.giveRise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __repr__(self):
        return str(self.person)


if __name__ == '__main__':
    rob = Manager('Rob Anderson', 100_000)
    print(rob)
    rob.giveRise(0.4)
    print(rob)
    rob.giveRise(0.1, )
    print(rob)
