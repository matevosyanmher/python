# reverse a string using coprehension

def reverse(text):
    return ''.join(reversed(text))


def isPalindrome(text):
    return text == reverse(text)


def find(text):
    return filter(isPalindrome, text)

print(reverse('madam'))
print(isPalindrome('madam'))