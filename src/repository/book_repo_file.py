from src.repository.book_repo import BookRepository


class BookRepositoryFile(BookRepository):
    def __init__(self, books_text_file):
        super().__init__()
        self.__file_name = books_text_file
        self.__load_data()

    def __load_data(self):
        file = open(self.__file_name, "rt")
        for line in file.readlines():
            book_id, author, title = line.split(", ")
            title = title.removesuffix("\n")
            super().add_book(int(book_id), author, title)
        file.close()

    def __save_data(self):
        file = open(self.__file_name, "wt")
        for book in super().list_of_books:
            file.write(f"{book.book_id}, {book.author}, {book.title}\n")
        file.close()

    def add_book(self, book_id, author, title):
        super(BookRepositoryFile, self).add_book(book_id, author, title)
        self.__save_data()

    def remove_book(self, book_id):
        super(BookRepositoryFile, self).remove_book(book_id)
        self.__save_data()

    def update_book(self, book_id, new_book):
        super(BookRepositoryFile, self).update_book(book_id, new_book)
        self.__save_data()
