def search4vowels(word: str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set("aeiou")
    return vowels.intersection(set(word))


print(search4vowels('galaxy'))


def search4letters(phrase: str, letter: str = "aeiou") -> set:
    """Return a set of letters found in phrase"""
    return set(letter).intersection(set(phrase))


print(search4letters("galaxy", "yaz"))
search4letters(phrase="galaxy", letter="xyz")
