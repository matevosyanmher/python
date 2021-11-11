import os

outfile = open("Homework_4_build_in.py", "x")
for filename in os.listdir("."):
    if filename.endswith(".py") or filename != "test.py":
        with open(filename, 'r') as readfile:
            for line in readfile:
                outfile.write(line)
                # print(os.path.join(os.listdir("."), filename))
        outfile.write("\n")
        continue
    else:
        continue
