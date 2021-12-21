import re
from pyxll import xl_func


@xl_func
def regexp(string):
    # string = "Համաձայն Հ/Ա Ա43770154, ա12345678901, 4377015405 ա/թ. 03/11/21 (Online banking 321656, dd 12/099/2021)"
    new_string = re.sub('\(.*\)', '()', string)
    regex = r'[Ա|ա|\s]\d(?: ?\d){3,9}'

    matches = re.findall(regex, new_string)

    output = []
    for match in matches:
        match = match.replace(" ", "", 2)
        output.append(match)

    return output


# regexp(r"Համաձայն Հ/Ա Ա43770154, ա12345678901, 43770 15405 ա/թ. 03/11/21 (Online banking 321656, dd 12/099/2021)")
