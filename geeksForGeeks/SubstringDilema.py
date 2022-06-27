def test_1(string=""):
    # initializing the substring
    substring = ""
    test_list = []
    initial = 0

    for _ in string:
        for i in range(initial, len(string)):
            substring += string[i]

            if substring.count(string[i]) > 1:
                test_list.append(substring[:-1])
                substring = ""
                initial = i + 1
                break

    maxi_word = ""
    for word in test_list:
        if len(word) > len(maxi_word):
            maxi_word = word
    return maxi_word


print(test_1("anahitvardumyan"))
