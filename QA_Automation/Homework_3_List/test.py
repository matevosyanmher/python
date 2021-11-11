import os

outfile = open("aaa.txt", "x")
for filename in os.listdir("."):

    # if filename.endswith(".py"):
        with open(filename, 'r') as readfile:
            for line in readfile:
                outfile.write(line)
        outfile.write("\n")
        # continue
    # else:
    #     continue
