list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
a = list_numbers[0]
a_pos = 0

for pos, i in enumerate(list_numbers):
    if i >= a:
        a = i
        a_pos = pos
list_numbers[a_pos] = list_numbers[-1]
list_numbers[-1] = a

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
