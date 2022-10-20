
class Book:
    def __init__(self, book_id, author, title):
        """This function initiates a book object.
        :param book_id: unique string
        :param author: string
        :param title: string
        """
        self.__book_id = book_id
        self.__author = author
        self.__title = title

    @property
    def book_id(self):
        """This function returns the book_id of a book.
        :return: string
        """
        return self.__book_id

    @book_id.setter
    def book_id(self, book_id):
        """This function sets a book_id to a book.
        :param book_id: string
        :return: -
        """
        self.__book_id = book_id

    @property
    def author(self):
        """This function returns the author of a book.
        :return: string
        """
        return self.__author

    @author.setter
    def author(self, author):
        """This function sets a author to a book.
        :param author: string
        :return: -
        """
        self.__author = author

    @property
    def title(self):
        """This function returns the title of a book.
        :return: string
        """
        return self.__title

    @title.setter
    def title(self, title):
        """This function sets a title to a book.
        :param title: string
        :return: -
        """
        self.__title = title

    def __str__(self):
        """This function converts a book to string representation.
        :return: a string representation of a object book-
        """
        return f"Book ID: {self.__book_id}, Author: {self.__author}, Title: {self.__title}"