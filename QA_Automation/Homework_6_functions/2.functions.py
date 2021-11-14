# 2. Write a function that takes a list and returns a new list with unique elements of the first list

def unic_list(lst):
    unic_lst = set(lst)
    return unic_lst


listNo1 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
print(unic_list(listNo1))
