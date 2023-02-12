class Book:

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, int) and value > 0:
            self._pages = value
        else:
            raise ValueError("Страницы должны быть положительным числом")

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if isinstance(value, float) and value > 0.0:
            self._duration = value
        else:
            raise ValueError("Длительность должна быть положительным числом")

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Длительность {self._duration} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"



pb = PaperBook("Война и Мир", "Лев Толстой", 1225)
ab = AudioBook("Война и Мир", "Лев Толстой", 35.5)

#Проверка атрибутов
print(pb.name) 
print(pb.author) 
print(pb.pages) 

print(ab.name) 
print(ab.author) 
print(ab.duration) 

#Проверка методов
print(pb)
print(ab) 

print(repr(pb))
print(repr(ab)) 

#Проверка пункта 3 и 4
try:
    pb.name = "Анна Каренина"
except AttributeError as e:
    print(e)

try:
    pb.author = "Федор Михайлович Достоевский"
except AttributeError as e:
    print(e) 
    
try:
    pb.pages = -10
except ValueError as e:
    print(e)