from person import Person, Manager
import shelve
import pprint

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=200000)
tom = Manager('Tom Jones', 50000)

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

db = shelve.open('persondb')
print(len(db))
list(map(print, db.items()))
for k, v in db.items():
    print(k, ',', v)

print(list(db.keys()))
bob = db['Bob Smith']
print(bob.lastName())
for key in sorted(db):
    print(key, '=>', db[key])
db.close()
