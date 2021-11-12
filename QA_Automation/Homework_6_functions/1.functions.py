import os, string

with open("functions", "rb") as f:
    for file in os.walk(".py"):
       file.open("2.functions.py")