import json
from src.repository.book_repo import BookRepository


class BookRepositoryJSON(BookRepository):
    def __init__(self, books_text_file):
        super(BookRepositoryJSON, self).__init__()
        self.__file_name = books_text_file
        self.__load_data()

    def __load_data(self):
        file = open(self.__file_name, "r")
        for element in json.load(file):
            super().add_book(int(element["id"]), element["author"], element["title"])
        file.close()

    def __save_data(self):
        file = open(self.__file_name, "w")
        content = []
        for book in super().list_of_books:
            dictionary = {"id": book.book_id, "author": book.author, "title": book.title}
            content.append(dictionary)
        json.dump(content, file, indent=4)
        file.close()

    def add_book(self, book_id, author, title):
        super(BookRepositoryJSON, self).add_book(book_id, author, title)
        self.__save_data()

    def remove_book(self, book_id):
        super(BookRepositoryJSON, self).remove_book(book_id)
        self.__save_data()

    def update_book(self, book_id, new_book):
        super(BookRepositoryJSON, self).update_book(book_id, new_book)
        self.__save_data()
