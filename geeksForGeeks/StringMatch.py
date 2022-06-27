import random


def string_generator(str_len):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    new_str = ''
    for i in range(str_len):
        new_str += alphabet[random.randrange(len(alphabet))]
    return new_str


# print(string_generator(3))

def string_match_score(goal, testStr):
    score = 0
    for i in range(len(goal)):
        if goal[i] == testStr[i]:
            score += 1
    return score / len(goal)  # return the score


def main():
    goal = 'mher'
    test_str = string_generator(len(goal))
    score = string_match_score(goal, test_str)
    best_score = 0
    iter_count = 0

    while score <= 1:
        iter_count += 1
        if score > best_score:
            best_score = score
            print(test_str)
            print(score)
            print(iter_count)
            if best_score == 1:
                break
        test_str = string_generator(len(goal))
        score = string_match_score(goal, test_str)


main()
