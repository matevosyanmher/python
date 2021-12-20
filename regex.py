import re

myString = "Համաձայն Հ/Ա Ա43770154, ա12345678901, 4377015405 ա/թ. 03/11/21 (Online banking 321656, dd 12/099/2021)"
newString = re.sub('\(.*\)', '()', myString)
regex = r"[աԱ]?\d{6,10}"

match = re.findall(regex, newString)

print(match)
print(newString)
# print('#################')
# match = "".join(match)
# match.strip()
# print(match)
