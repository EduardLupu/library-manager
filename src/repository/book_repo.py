from src.domain.book import Book
from src.domain.container import Container
from src.domain.validators import Validators


class BookRepository:
    def __init__(self):
        self.__list_of_books = Container()

    @property
    def list_of_books(self):
        """This function returns the list of books.
        :return: the list of books
        """
        return self.__list_of_books

    def check_if_book_id_is_unique(self, unchecked_id):
        """This function checks if the unchecked_id is unique or not.
        :param unchecked_id: string
        :return: True if unchecked_id is unique, False if not.
        """
        for book in self.__list_of_books:
            if book.book_id == unchecked_id:
                return False
        return True

    def add_book(self, book_id, author, title):
        """This function adds a book to the list of books.

        :return: -
        """
        if self.check_if_book_id_is_unique(book_id) is True:
            new_book = Book(book_id, author, title)
            self.__list_of_books.append(new_book)
        else:
            Validators.handle_not_unique_id()

    def remove_book(self, book_id):
        """This function removes a book from the list of books.

        :param book_id: integer
        :return: -
        """
        if self.check_if_book_id_is_unique(book_id) is True:
            Validators.entity_not_in_list()
        else:
            for book in self.__list_of_books:
                if book.book_id == book_id:
                    book_to_be_removed = book
                    self.__list_of_books.remove(book_to_be_removed)
                    return

    def update_book(self, book_id, new_book):
        """This function updates a book with a new one.

        :param book_id: int
        :param new_book: a book object, class <Book>
        :return: -
        """
        index = -1
        if self.check_if_book_id_is_unique(book_id) is True:
            Validators.id_not_in_list()
        elif self.check_if_book_id_is_unique(new_book.book_id):
            for book in self.list_of_books:
                index += 1
                if book.book_id == book_id:
                    self.__list_of_books[index] = new_book
                    return
        else:
            Validators.handle_not_unique_id()
