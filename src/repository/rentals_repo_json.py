import json
from src.repository.rentals_repo import RentalRepository


class RentalRepositoryJSON(RentalRepository):
    def __init__(self, rentals_text_file):
        super(RentalRepositoryJSON, self).__init__()
        self.__file_name = rentals_text_file
        self.__load_data()

    def __load_data(self):
        file = open(self.__file_name, "r")
        for element in json.load(file):
            super().add_rental(int(element["rental_id"]), int(element["book_id"]), int(element["client_id"]),
                               element["rent_date"], element["returned_date"])
        file.close()

    def __save_data(self):
        file = open(self.__file_name, "w")
        content = []
        for rental in super().list_of_rentals:
            dictionary = {"rental_id": rental.rental_id, "book_id": rental.book_id, "client_id": rental.client_id,
                          "rent_date": rental.rented_date, "returned_date": rental.returned_date}
            content.append(dictionary)
        json.dump(content, file, indent=4)
        file.close()

    def add_rental(self, rental_id, book_id, client_id, rent_date, returned_date):
        super(RentalRepositoryJSON, self).add_rental(rental_id, book_id, client_id, rent_date, returned_date)
        self.__save_data()

    def return_book(self, rental_id):
        super(RentalRepositoryJSON, self).return_book(rental_id)
        self.__save_data()
