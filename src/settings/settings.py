from src.repository.book_repo import BookRepository
from src.repository.book_repo_file import BookRepositoryFile
from src.repository.book_repo_binary import BookRepositoryBinary
from src.repository.client_repo import ClientRepository
from src.repository.client_repo_binary import ClientRepositoryBinary
from src.repository.client_repo_file import ClientRepositoryFile
from src.repository.rentals_repo import RentalRepository
from src.repository.rentals_repo_file import RentalRepositoryFile
from src.repository.rentals_repo_binary import RentalRepositoryBinary
from src.repository.book_repo_json import BookRepositoryJSON
from src.repository.client_repo_json import ClientRepositoryJSON
from src.repository.rentals_repo_json import RentalRepositoryJSON
from src.repository.book_repo_database import BookRepositoryDatabase
from src.repository.client_repo_database import ClientRepositoryDatabase
from src.repository.rental_repo_database import RentalRepositoryDatabase
from configparser import ConfigParser
import os


class Settings:
    def __init__(self):
        config = ConfigParser()
        repo_location = os.path.abspath(__file__)
        repo_location = repo_location.removesuffix(r"settings\settings.py")
        repo_location = repo_location + "repository\\"
        settings_location = os.path.abspath(__file__)
        settings_location = settings_location.removesuffix(".py")
        settings_location = settings_location + ".properties"
        config.read(settings_location)
        option = 1
        option = input(
        "1. In-memory\n2. Files\n3. Binary\n4. JSON\n5. Database sqlite\nNumber of the repository you want to use: ")

        if option == "1":
            self.book_repo = BookRepository()
            self.client_repo = ClientRepository()
            self.rental_repo = RentalRepository()
        elif option == "2":
            books_file = config.get("options", "booksf")
            clients_file = config.get("options", "clientsf")
            rentals_file = config.get("options", "rentalsf")
            self.book_repo = BookRepositoryFile(repo_location + books_file)
            self.client_repo = ClientRepositoryFile(repo_location + clients_file)
            self.rental_repo = RentalRepositoryFile(repo_location + rentals_file)
        elif option == "3":
            books_file = config.get("options", "booksb")
            clients_file = config.get("options", "clientsb")
            rentals_file = config.get("options", "rentalsb")
            self.book_repo = BookRepositoryBinary(repo_location + books_file)
            self.client_repo = ClientRepositoryBinary(repo_location + clients_file)
            self.rental_repo = RentalRepositoryBinary(repo_location + rentals_file)
        elif option == "4":
            books_file = config.get("options", "booksj")
            clients_file = config.get("options", "clientsj")
            rentals_file = config.get("options", "rentalsj")
            self.book_repo = BookRepositoryJSON(repo_location + books_file)
            self.client_repo = ClientRepositoryJSON(repo_location + clients_file)
            self.rental_repo = RentalRepositoryJSON(repo_location + rentals_file)
        elif option == "5":
            books_file = config.get("options", "booksd")
            clients_file = config.get("options", "clientsd")
            rentals_file = config.get("options", "rentalsd")
            self.book_repo = BookRepositoryDatabase(repo_location + books_file)
            self.client_repo = ClientRepositoryDatabase(repo_location + clients_file)
            self.rental_repo = RentalRepositoryDatabase(repo_location + rentals_file)
        else:
            raise Exception("Type a number between 1 and 5!")


    def get_repos(self):
        return self.book_repo, self.client_repo, self.rental_repo
