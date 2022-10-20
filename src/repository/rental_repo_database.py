import datetime
import sqlite3
from src.repository.rentals_repo import RentalRepository


class RentalRepositoryDatabase(RentalRepository):
    def __init__(self, rentals_text_file):
        super(RentalRepositoryDatabase, self).__init__()
        self.__file_name = rentals_text_file
        self.__load_data()

    def __load_data(self):
        self.connection = sqlite3.connect(self.__file_name)
        self.cursor = self.connection.cursor()
        self.query = """
        CREATE TABLE IF NOT EXISTS rentals (
          id INTEGER PRIMARY KEY,
          book_id INTEGER,
          client_id INTEGER,
          rent_date TEXT,
          returned_date TEXT
        );
        """
        self.cursor.execute(self.query)
        self.connection.commit()
        self.cursor.execute(self.query)
        self.connection.commit()
        self.cursor.execute("""SELECT * FROM rentals;""")
        rows = self.cursor.fetchall()
        for rental in rows:
            super().add_rental(rental[0], rental[1], rental[2], rental[3], rental[4])

    def add_rental(self, rental_id, book_id, client_id, rent_date, returned_date):
        super(RentalRepositoryDatabase, self).add_rental(rental_id, book_id, client_id, rent_date, returned_date)
        self.cursor.execute("""INSERT INTO rentals VALUES (?, ?, ?, ?, ?);""",
                            (rental_id, book_id, client_id, rent_date, returned_date))
        self.connection.commit()

    def return_book(self, rental_id):
        super(RentalRepositoryDatabase, self).return_book(rental_id)
        date = datetime.datetime.now()
        self.cursor.execute("""UPDATE rentals SET returned_date=? WHERE id=?;""",
                            (date.strftime("%d.%m.%Y"), rental_id))
        self.connection.commit()
