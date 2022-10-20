from src.repository.book_repo import BookRepository
import pickle


class BookRepositoryBinary(BookRepository):
    def __init__(self, books_text_file):
        super().__init__()
        self.__file_name = books_text_file
        self.__load_data()

    def __load_data(self):
        file = open(self.__file_name, "rb")
        books = pickle.load(file)
        for book in books:
            super().add_book(book.book_id, book.author, book.title)
        file.close()

    def __save_data(self):
        file = open(self.__file_name, "wb")
        pickle.dump(super().list_of_books, file)
        file.close()

    def add_book(self, book_id, author, title):
        super(BookRepositoryBinary, self).add_book(book_id, author, title)
        self.__save_data()

    def remove_book(self, book_id):
        super(BookRepositoryBinary, self).remove_book(book_id)
        self.__save_data()

    def update_book(self, book_id, new_book):
        super(BookRepositoryBinary, self).update_book(book_id, new_book)
        self.__save_data()
