import os

outfile = open("xxx.txt", "x")
for filename in os.listdir("."):
    if filename != "xxx.txt" or filename.endswith(".py"):
        with open(filename, 'r') as readfile:
            for line in readfile:
                outfile.write(line + "\n")
                # print(os.path.join(os.listdir("."), filename))
        continue
    else:
        continue
