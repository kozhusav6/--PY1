from pprint import pprint

bdho = [
    {
        'bin': n,
        'dec': dec(n),
        'hex': hex(n),
        'oct': oct(n)
    }
    for n in range(0, 16)
]

pprint(bdho)
# TODO решить с помощью list comprehension и распечатать его
