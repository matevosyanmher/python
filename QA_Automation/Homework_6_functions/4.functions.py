# 4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters

def string_calculator(str):
    upper_str = 0
    lower_str = 0
    special_characters = "!@#$%^&*()-+?_=,<>/"
    for i in str:
        if i.isupper() and i not in special_characters:
            upper_str += 1
        elif i.islower() and i not in special_characters:
            lower_str += 1
        else:
            pass
    return print(f"No. of Lower case characters : {lower_str}\nNo. of Upper case characters : {upper_str}")


string_calculator(str=input("Input any string that contain uppercase and lowercase letters: "))
