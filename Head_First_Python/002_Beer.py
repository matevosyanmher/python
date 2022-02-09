word = "bottles"
for beerNumber in range(99, 0, -1):
    print(beerNumber, word, "of beer in the wall.")
    print(beerNumber, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beerNumber == 1:
        print("No mere bottles of beer on the wall.")
    else:
        newNumber = beerNumber - 1
        if newNumber == 1:
            word = "bottle"
        print(newNumber, word, "of beer on the wall.")
    print()
