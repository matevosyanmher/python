import os
import csv
import pprint
from datetime import datetime

os.chdir(r"C:\Users\Mher\Desktop")


# with open('021_buzzers.csv') as data:
#     print(data.read())
#
# with open('021_buzzers.csv') as data:
#     for line in csv.reader(data):
#         print(line)
#
# with open('021_buzzers.csv') as data:
#     for line in csv.DictReader(data):
#         print(line['DESTINATION'].title().strip())
#

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('021_buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
pprint.pprint(flights)
print()

fts = {convert2ampm(k): v.title() for k, v in flights.items()}

flights2 = {dest: [k for k, v in flights.items() if v == dest] for dest in set(flights.values())}
pprint.pprint(flights2)
