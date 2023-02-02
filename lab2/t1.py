BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book(object):  # Описываем класс Book
    def __init__(self, id=None, title, pages):  # Инициализация экземпляра класса
        if (title == '') or (type(title) != str):  # Если название книги - пустая строка
            raise ValueError  # Выбрасываем исключение
        else:
            self.__title = title  # Иначе сохраняем название
        if (pages == '') or (type(pages) != str):  # То же самое для страниц
            self.__pages = 'Unknown'
        else:
            self.__pages = pages
        self.__id = id

    def tag(self):  # Реализация Taggable интерфейса
        return re.compile('[A-Z][a-z]+').findall(self.__title)  # Ищем слова с большой буквы и возвращаем их список

    def set_id(self, id):  # Функция установки кода книги
        self.__id = id

    def __str__(self):  # Преобразование в тип string
        return "[%s] %s '%s'" % (str(self.__id), self.__title, self.__pages)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__id}, {self.__title}, {self.__pages})"

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
