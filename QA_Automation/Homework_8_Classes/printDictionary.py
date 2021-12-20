iterator = 1


def print_dict(myDict, iterator, symbol=""):
    iterator += 1
    for k, v in myDict.items():
        print(symbol, k, ": ", end="")
        if type(v) == type(myDict):
            print("\n", end="")
            print_dict(v, iterator, (iterator * "\t"))
        else:
            print(v)


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Peter', 'age': '29', 'sex': 'Male',
              'parents': {"mam": "Gohar", "father": "Smbat", "brother": "Alik"}},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}

print_dict(people, iterator)
