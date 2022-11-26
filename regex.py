import re
import pyxll
import pandas

string = "Համաձայն Հ/Ա Ա43770154, 12345678901, 437701 11.02.2022    5405 ա/թ. 03/11/21 (Online banking 321656, dd 12/099/2021)"


def regexp(string):
    new_string = re.sub('\(.*\)', '()', string)
    regex = r'[Ա|ա|\s]\d(?: ?\d){4,10}'

    matches = re.findall(regex, string)

    output = []
    for match in matches:
        match1 = match.replace(" ", "", 2)
        output.append(match1)

    print(output)


regexp(string)
