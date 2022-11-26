X = 1


def nester():
    X = 2
    print(X)

    class C:
        X = 3
        print(X)

        def methode1(self):
            print(X)
            print(self.X)

        def methode2(self):
            X = 4
            print(X)
            self.X = 5
            print(self.X)

    I = C()
    I.methode1()
    I.methode2()


print(X)
nester()
print('-' * 140)
