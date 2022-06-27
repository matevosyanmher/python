class rec:
    pass


rec.name = 'Bob'
rec.age = 40
print(rec.name)
print(rec.age)
print()

x = rec()
y = rec()

x.name = 'Sue'

print(rec.name)
print(x.name)
print(y.name)

recLst = rec.__dict__
print(type(recLst))
print(recLst)

recLst = [name for name in rec.__dict__ if not name.startswith("__")]
print(recLst)

xLst = x.__dict__.keys()
print(xLst)
yLst = y.__dict__.keys()
print(yLst)
print()

print(x.age)
# print(x.__dict__["age"]) #KeyError
print(x.__class__)
print(rec.__bases__)
print()


def uppercase(obj):
    return obj.name.upper()


rec.methode = uppercase
print(x.methode())
print(y.methode())
print(rec.methode(x))
