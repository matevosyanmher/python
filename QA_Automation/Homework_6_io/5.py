# 5. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string
import os

if not os.path.exists("letters"):
    os.makedirs("letters")
letter = string.ascii_uppercase
for letter in string.ascii_uppercase:
    with open("C:\\Users\Mher\PycharmProjects\python\QA_Automation\Homework_6_io\letters\\" + letter + ".txt", "w") as f:
        f.write(letter)
        f.close
