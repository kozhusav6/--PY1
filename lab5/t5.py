import string
from random import sample

base = string.ascii_uppercase + string.ascii_lowercase + string.digits

def get_random_password(n: int = 8) -> str:
    if len(base) < n < 0:
        raise ValueError(f"Error, размер пароля должен быть больше [{0}] до [{len(base)}]")

    return ' '. join(sample(base, n))
  # TODO написать функцию генерации случайных паролей


print(get_random_password())
