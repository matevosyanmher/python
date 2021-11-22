# 3. Write a function to print the even numbers from a given list.

def even_numbers(numbers: list) -> list:
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)
        else:
            continue
    return result


numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_numbers(numbers1))
