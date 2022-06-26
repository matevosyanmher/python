from abc import ABCMeta, abstractmethod


class Supper(metaclass=ABCMeta):
    @abstractmethod
    def method(self):
        pass


class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass


class Sub(Super):
    def action(self):
        print('spam')
        872


x = Sub()
x.delegate()
