from src.utility.functions import gnome_sort

class RentalService:
    def __init__(self, rental_repo):
        self.__rental_repo = rental_repo

    def add_rental(self, rental_id, book_id, client_id, rent_date, returned_date):
        # adds a rental
        self.__rental_repo.add_rental(rental_id, book_id, client_id, rent_date, returned_date)

    def return_book(self, rental_id):
        # returns a book
        self.__rental_repo.return_book(rental_id)

    def get_all(self):
        return self.__rental_repo.list_of_rentals

    def rent_statistic(self):
        """This function creates a list in descending order of the most rented books.
        :return: dict
        """
        rent_times = {}
        for rental in self.get_all():
            if rental.book_id in rent_times.keys():
                rent_times[rental.book_id] += 1
            else:
                rent_times[rental.book_id] = 1
        # sorted(rent_times.items(), key=lambda item: item[1], reverse=True)
        gnome_sort(rent_times.items(), function=lambda item: item[1], reverse=True)
        return rent_times.items()

    def client_rent_statistic(self):
        """This function creates a list in descending order of the most active clients.
        :return: dict
        """
        rent_times = {}
        for rental in self.get_all():
            if rental.client_id in rent_times.keys():
                rent_times[rental.client_id] += 1
            else:
                rent_times[rental.client_id] = 1
        # sorted(rent_times.items(), key=lambda item: item[1], reverse=True)
        gnome_sort(rent_times.items(), function=lambda item: item[1], reverse=True)
        return rent_times.items()
