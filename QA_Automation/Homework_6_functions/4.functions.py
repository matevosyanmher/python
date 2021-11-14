# 4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters

def string_calculator(string1):
    upper_str = 0
    lower_str = 0
    special_characters = "!@#$%^&*()-+?_=,<>/"
    for i in string1:
        pass
    if i.isupper() and i not in special_characters:
        upper_str += 1
    elif i.islower() and i not in special_characters:
        lower_str += 1
    else:
        pass
    return (print(f"Lower: = {lower_str} & Upper: = {upper_str}"))

str = "aaaAA A"
string_calculator(str)
