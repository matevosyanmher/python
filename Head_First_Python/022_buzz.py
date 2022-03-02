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


#
# with open('021_buzzers.csv') as data:
#     ignore = data.readline()
#     flights = {}
#     for line in data:
#         k, v = line.strip().split(',')
#         flights[k] = v
# pprint.pprint(flights)
# # print()
#
with open('021_buzzers.csv') as data:
    ignore = data.readline()
    flights = {convert2ampm(k): v.title()
               for k, v in csv.reader(data)
               }
    print(flights)
# more_dest = []
# for dest in flights.values():
#     more_dest.append(dest)
# more_dest = [dest.title() for dest in flights.values()]
# print(more_dest)
# flight_times = [k for k in flights.keys()]
# print(flight_times)


lstTime = []
for k, v in flights.items():
    if v == 'Freeport':
        lstTime.append(k)
print(lstTime)

wests2 = [k for k, v in flights.items() if v == 'Freeport']
print(wests2)

for dest in set(flights.values()):
    print(dest, "->", [k for k, v in flights.items() if v == dest])

when = {}
for dest in set(flights.values()):
    when[dest] = [k for k, v in flights.items() if v == dest]
print(when)

when2 = {dest2: [k for k, v in flights.items() if v == dest2] for dest2 in set(flights.values())}
print(when2)
#
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = []
# for num in data:
#     if not num % 2 == 0:
#         evens.append(num)
# print(evens)
#
# evens2 = [nums for nums in data if nums % 2 != 0]
# print(evens2)
#
# data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
# words = []
# for num in data:
#     if isinstance(num, str):
#         words.append(num)
# print(words)
#
# words2 = [num for num in data if isinstance(num, str)]
# print(words2)
#
# data = list('So long and thanks for all the fish'.split())
# title = []
# for word in data:
#     title.append(word.title())
# print(title)
#
# title = [word.title() for word in data]
# print(title)
