from src.domain.rental import Rental
from src.domain.container import Container
from src.domain.validators import Validators
from openpyxl import load_workbook
import datetime


class RentalRepository:
    def __init__(self):
        self.__list_of_rentals = Container()

    @property
    def list_of_rentals(self):
        """This function returns the list of rentals.
        :return: the list of rentals
        """
        return self.__list_of_rentals

    def load_data(self):
        workbook = load_workbook("D:\\GitHub\\a9-luckytoef\\src\\repository\\data\\rentals_data.xlsx")
        sheet = workbook.active
        for row in sheet.rows:
            self.__list_of_rentals.append(Rental(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value))

    def check_if_book_rented(self, book_id):
        """This function checks if the book is in rent right now.
        :param book_id: int
        :return: True/False
        """
        for rental in self.list_of_rentals:
            if rental.book_id == book_id and rental.returned_date is None:  # If the book is rented.
                return True
        return False

    def check_if_rental_id_is_unique(self, unchecked_id):
        """This function checks if the unchecked_id is unique or not.
        :param unchecked_id: string
        :return: True if unchecked_id is unique, False if not.
        """
        for rental in self.list_of_rentals:
            if rental.rental_id == unchecked_id:
                return False
        return True

    def add_rental(self, rental_id, book_id, client_id, rent_date, returned_date):
        if self.check_if_rental_id_is_unique(rental_id) is False:
            Validators.handle_not_unique_id()
        elif self.check_if_book_rented(book_id) is True:
            Validators.book_is_rented()
        else:
            self.__list_of_rentals.append(Rental(rental_id, book_id, client_id, rent_date, returned_date))

    def return_book(self, rental_id):
        date = datetime.datetime.now()
        if self.check_if_rental_id_is_unique(rental_id) is True:
            Validators.id_not_in_list()
        else:
            for rental in self.__list_of_rentals:
                if rental.rental_id == rental_id:
                    rental.returned_date = date.strftime("%d.%m.%Y")
                    return
