
class Rental:
    def __init__(self, rental_id, book_id, client_id, rented_date, returned_date):
        self.__rental_id = rental_id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__returned_date = returned_date

    @property
    def rental_id(self):
        return self.__rental_id

    @rental_id.setter
    def rental_id(self, value):
        self.__rental_id = value

    @property
    def book_id(self):
        return self.__book_id

    @book_id.setter
    def book_id(self, value):
        self.__book_id = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = value

    @property
    def rented_date(self):
        return self.__rented_date

    @rented_date.setter
    def rented_date(self, value):
        self.__rented_date = value

    @property
    def returned_date(self):
        return self.__returned_date

    @returned_date.setter
    def returned_date(self, value):
        self.__returned_date = value

    def __str__(self):
        """This function converts a book to string representation.
        :return: a string representation of a object book-
        """
        return f"Rental ID: {self.__rental_id}, Book ID: {self.__book_id}, Client ID: {self.__client_id}," \
               f" Rented Date: {self.__rented_date}, Returned Date: {self.__returned_date}"
