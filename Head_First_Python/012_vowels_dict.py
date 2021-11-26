vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide word to search in vowels: ")
found = {}
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
print(found)

for k, v in sorted(found.items()):
    print(k, "was found", v, "time(s)")
