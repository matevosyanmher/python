# 3. Write a Python program to copy the contents of a file to another file
with open("file_name.txt", "r") as firstFile, open("write_file.txt", "a") as secondFile:
    for line in firstFile:
        secondFile.write(line)
