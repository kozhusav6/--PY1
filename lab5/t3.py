from random import sample

def get_unique_list_numbers(a: int, b: int, c: int) -> list[int]:
    if a > b:
        raise ValueError("Error")
    elif c > a % 1 + b % 1:
        raise ValueError("Error")

    return sample(range(a, b+1), c)


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
