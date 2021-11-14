# 2. Write a program to find the longest words
file = open("file_name.txt", "r")


def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    print(words)
    max_len = len(max(words, key=len))


    return [word for word in words if len(word) == max_len]


print(longest_word('file_name.txt'))
