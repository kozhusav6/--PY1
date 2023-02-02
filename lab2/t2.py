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
    def __init__(self, pages, title, id=None):  # Инициализация экземпляра класса
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
        return "[%s] %s '%s'" % (str(self.__id), self.__pages, self.__title)

# TODO написать класс Library
class Library(object):  # Описание класса Library
    code = 1  # Статическая переменная класса, код книги

    def __init__(self,):  # Инициализация экземпляра
        self.__books = []  # Список книг, изначально пустой

    def __iadd__(self, b):  # Перегрузка оператора +=
        b.set_code(Library.code)  # Устанавливаем книге код
        Library.code += 1  # Увеличиваем код на 1
        self.__books.append(b)  # Дополняем список книг
        return self  # Возвращаем новую библиотеку

    def __iter__(self):  # Преобразование в итерируемый объект
        return iter(self.__books)  # Преобразуем список книг в итератор


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
