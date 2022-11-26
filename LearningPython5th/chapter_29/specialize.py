class Supper:
    def method(self):
        print('In Supper method')

    def delegate(self):
        self.action()


class Inheritor(Supper):
    pass


class Replacer(Supper):
    def method(self):
        print('In Replacer.method')


class Extender(Supper):
    def method(self):
        print('starting Extender.method')
        Supper.method(self)
        print('end Extender.method')


class Provider(Supper):
    def action(self):
        print('in Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
    y = Extender()
    y.delegate()
