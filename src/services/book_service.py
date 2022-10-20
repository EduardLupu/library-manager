
class BookService:
    def __init__(self, book_repo):
        self.__book_repo = book_repo

    def add_book(self, book_id, author, title):
        # adds a book
        self.__book_repo.add_book(book_id, author, title)

    def remove_book(self, book_id):
        # removes a book
        self.__book_repo.remove_book(book_id)

    def update_book(self, book_id, new_book):
        # updates a book with a new one
        self.__book_repo.update_book(book_id, new_book)

    def get_all(self):
        return self.__book_repo.list_of_books

    def find_book_by_id(self, id):
        """This function returns the book with the specified id.
        :param id:int
        :return:book
        """
        for book in self.get_all():
            if book.book_id == id:
                return book
        return None

    def search_book(self, data_of_book):
        """This function search for books which have a common data.
        :param data_of_book: any data of the book(id/ title/ author)
        :return:
        """
        book_list = []
        found_data = 0
        if data_of_book.isnumeric():
            for book in self.get_all():
                if book.book_id == int(data_of_book) or data_of_book in book.title.lower():
                    book_list.append(book)
                    found_data = 1
        else:
            for book in self.get_all():
                if data_of_book in book.title.lower() or data_of_book in book.author.lower():
                    book_list.append(book)
                    found_data = 1
        if found_data:
            return book_list
        return None