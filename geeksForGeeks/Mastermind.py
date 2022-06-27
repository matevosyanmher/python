import random


def code_generator():
    gen_code = []

    for i in range(4):
        gen_code.append(random.randint(0, 9))

    return gen_code


# print(code_generator())


def user_code():
    code_user = input("enter 4 digit code: ")
    return code_user


def comparison():
    gen_code = code_generator()
    print(gen_code)
    i = 0
    while i < 10:
        result = ""
        input_code = [int(c) for c in user_code()]
        print(input_code)
        if len(input_code) != 4:
            print("Enter only 4 digit number")
            continue

        if gen_code == input_code:
            print("you won!!!" + " " + " ".join(str(x) for x in gen_code))
            break

        for element in input_code:
            if element in gen_code:
                if input_code.index(element) == gen_code.index(element):
                    result += "R"
                else:
                    result += "Y"
            else:
                result += "B"
        print(result)

        i += 1
    else:
        print("you have tried more then 10 times")


comparison()

