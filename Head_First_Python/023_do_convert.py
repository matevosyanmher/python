import csv
from datetime import datetime
from pprint import pprint
import os

os.chdir(r"C:\Users\Mher\Desktop")


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('021_buzzers.csv') as data:
    ignore = data.readline()
    fts = {convert2ampm(k): v.title() for k, v in csv.reader(data)}

when = {dest: [k for k, v in fts.items() if v == dest] for k, v in fts.items() for dest in set(fts.values())}
pprint(when)
