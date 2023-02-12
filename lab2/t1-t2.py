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
class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id!r}, name={self.name!r}, pages={self.pages!r})"



#Проверка
books = [Book(**book_data) for book_data in BOOKS_DATABASE]
for book in books:
    print(book)
    
###############################################################################
#                                      PART 2                                 #
###############################################################################

class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for i, book in enumerate(self.books):
            if book.id == book_id:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")

#Проверка
library = Library()
print(library.get_next_book_id())

book = Book(1, "Война и Мир", 1225)
library.books.append(book)
print(library.get_next_book_id())

try:
    index = library.get_index_by_book_id(2)
except ValueError as e:
    print(e)

index = library.get_index_by_book_id(1)
print(index)
