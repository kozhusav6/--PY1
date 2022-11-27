BYTES_ONE_CHAR = 1  # размер одного символа в байтах

# никаких магических чисел
pages = 100
lines = 50
chars = 25

total_chars = chars * lines * pages
total_bytes = total_chars

disk_size = 1.44 * 1024**2

N = disk_size/ total_bytes

print(round(disk_size/ total_bytes, 0))  # TODO найти количество книг, которое поместится на дискете
