import shelve

db = shelve.open('persondb')
for key in sorted(db):
    print(key, '=>', db[key])
#
sue = db['Sue Jones']
sue.giveRise(0.1)
db['Sue Jones'] = sue

print()

list(map(print, db.items()))
# db.clear()
db.close()
