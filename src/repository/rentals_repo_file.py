from src.repository.rentals_repo import RentalRepository


class RentalRepositoryFile(RentalRepository):
    def __init__(self, rentals_text_file):
        super().__init__()
        self.__file_name = rentals_text_file
        self.__load_data()

    def __load_data(self):
        file = open(self.__file_name, "rt")
        for line in file.readlines():
            if ", " in line:
                rental_id, book_id, client_id, rent_date, returned_date = line.split(", ")
                returned_date = returned_date.removesuffix("\n")
                super().add_rental(int(rental_id), int(book_id), int(client_id), rent_date, returned_date)
        file.close()

    def __save_data(self):
        file = open(self.__file_name, "wt")
        for rental in super().list_of_rentals:
            file.writelines(f"{rental.rental_id}, {rental.book_id}, {rental.client_id}, {rental.rented_date}, "
                            f"{rental.returned_date}\n")
        file.close()

    def add_rental(self, rental_id, book_id, client_id, rent_date, returned_date):
        super(RentalRepositoryFile, self).add_rental(rental_id, book_id, client_id, rent_date, returned_date)
        self.__save_data()

    def return_book(self, rental_id):
        super(RentalRepositoryFile, self).return_book(rental_id)
        self.__save_data()
