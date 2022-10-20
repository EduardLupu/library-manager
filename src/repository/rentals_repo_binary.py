from src.repository.rentals_repo import RentalRepository
import pickle


class RentalRepositoryBinary(RentalRepository):
    def __init__(self, rentals_text_file):
        super().__init__()
        self.__file_name = rentals_text_file
        self.__save_data()

    def __load_data(self):
        file = open(self.__file_name, "rb")
        rentals = pickle.load(file)
        for rental in rentals:
            super().add_rental(rental.rental_id, rental.book_id, rental.client_id, rental.rented_date, rental.returned_date)
        file.close()

    def __save_data(self):
        file = open(self.__file_name, "wb")
        pickle.dump(super().list_of_rentals, file)
        file.close()

    def add_rental(self, rental_id, book_id, client_id, rent_date, returned_date):
        super(RentalRepositoryBinary, self).add_rental(rental_id, book_id, client_id, rent_date, returned_date)
        self.__save_data()

    def return_book(self, rental_id):
        super(RentalRepositoryBinary, self).return_book(rental_id)
        self.__save_data()