from src.domain.book import Book
from src.domain.client import Client
from src.undo.undo import UndoRedoObject
import datetime


class ConsoleUI:
    def __init__(self, book_service, client_service, rental_service, undo_action):
        """ This function initiates a library.

        """
        self.__book_service = book_service
        self.__client_service = client_service
        self.__rental_service = rental_service
        self.__undo_redo_service = undo_action

    @staticmethod
    def __read_option():
        """This function input a command from the user.
        :return: string
        """
        __option = input(">>>")
        return __option

    def __display_books(self):
        """This function displays every book in the library.
        :return: -
        """
        for book in self.__book_service.get_all():
            print(book)

    def __display_clients(self):
        """This function displays every client in the library.
        :return: -
        """
        for client in self.__client_service.get_all():
            print(client)

    def __display_rentals(self):
        """This function displays every rental in the library.
        :return: -
        """
        for rental in self.__rental_service.get_all():
            print(rental)

    @staticmethod
    def __menu():
        """This function displays the menu.
        :return: -
        """
        print(" \n\n================================ MENU ================================")
        print("1. Add book\n2. Add client\n3. Remove book\n4. Remove client\n5. Display books")
        print("6. Display clients\n7. Display rentals\n8. Update book\n9. Update client")
        print("10. Rent a book\n11. Return a book\n12. Search book\n13. Search client")
        print("14. Most rented books\n15. Most active clients\n16. Undo\n17. Redo \n0. Exit")

    def __execute_option_add(self, option):
        """This function executes the ADD option.

        :param option: string
        :return:
        """
        if "add book" in option:
            book_id = int(input("Book ID: "))
            author = input("Author: ")
            title = input("Title: ")
            self.__book_service.add_book(book_id, author, title)
            undo_redo_operation = UndoRedoObject(lambda: self.__book_service.remove_book(book_id),
                                                 lambda: self.__book_service.add_book(book_id, author, title))
            self.__undo_redo_service.add_operation(undo_redo_operation)
        elif "add client" in option:
            client_id = int(input("Client ID: "))
            name = input("Name: ")
            self.__client_service.add_client(client_id, name)
            undo_redo_operation = UndoRedoObject(lambda: self.__book_service.remove_client(client_id),
                                                 lambda: self.__book_service.add_client(client_id, name))
            self.__undo_redo_service.add_operation(undo_redo_operation)
        else:
            print("Invalid input!")

    def __execute_option_display(self, option):
        """This function executes the DISPLAY option.

        :param option: string
        :return:
        """
        if "display books" in option:
            self.__display_books()
        elif "display clients" in option:
            self.__display_clients()
        elif "display rentals" in option:
            self.__display_rentals()
        else:
            print("Invalid input!")

    def __execute_option_remove(self, option):
        """This function executes the REMOVE option.

        :param option: string
        :return:
        """
        if "remove book" in option:
            book_id = int(input("Enter the Book ID of the book that you want to remove: "))
            book = self.__book_service.find_book_by_id(book_id)
            undo_redo_operation = UndoRedoObject(
                lambda: self.__book_service.add_book(book.book_id, book.author, book.title),
                lambda: self.__book_service.remove_book(book_id))
            self.__undo_redo_service.add_operation(undo_redo_operation)
            self.__book_service.remove_book(book_id)
        elif "remove client" in option:
            client_id = int(input("Enter the Client ID of the client that you want to remove:"))
            client = self.__client_service.find_client_by_id(client_id)
            undo_redo_operation = UndoRedoObject(
                lambda: self.__client_service.add_client(client.client_id, client.name),
                lambda: self.__client_service.remove_client(client_id))
            self.__undo_redo_service.add_operation(undo_redo_operation)
            self.__client_service.remove_client(client_id)
        else:
            print("Invalid input!")

    def __execute_option_update(self, option):
        if "update book" in option:
            book_id_to_be_updated = int(input("Enter the Book ID of the book that you want to update: "))
            book_id = int(input("Enter the updated book \n Book ID: "))
            author = input("Author: ")
            title = input("Title: ")
            book_to_update = self.__book_service.find_book_by_id(book_id_to_be_updated)
            self.__book_service.update_book(book_id_to_be_updated, Book(book_id, author, title))
            undo_redo_operation = UndoRedoObject(
                lambda: self.__book_service.update_book(book_id, book_to_update),
                lambda: self.__book_service.update_book(book_id, Book(book_id, author, title)))
            self.__undo_redo_service.add_operation(undo_redo_operation)
        elif "update client" in option:
            client_id_to_be_updated = int(input("Enter the Client ID of the client that you want to update: "))
            client_id = int(input("Enter the updated client \n Client ID: "))
            name = input("Name: ")
            client_to_update = self.__client_service.find_client_by_id(client_id_to_be_updated)
            self.__client_service.update_client(client_id_to_be_updated, Client(client_id, name))
            undo_redo_operation = UndoRedoObject(
                lambda: self.__client_service.update_client(client_id, client_to_update),
                lambda: self.__client_service.update_client(client_id, Client(client_id, name)))
            self.__undo_redo_service.add_operation(undo_redo_operation)
        else:
            print("Invalid input!")

    def __execute_option_search(self, option):
        if "search book" in option:
            data_of_book = input("Enter any field of the book that you would like to search: ")
            book_list = self.__book_service.search_book(data_of_book.lower())
            if book_list is not None:
                for book in book_list:
                    print(book)
            else:
                print("No matching data found in the database.")
        elif "search client" in option:
            data_of_client = input("Enter any field of the client that you would like to search: ")
            client_list = self.__client_service.search_client(data_of_client.lower())
            if client_list is not None:
                for client in client_list:
                    print(client)
            else:
                print("No matching data found in the database.")
        else:
            print("Invalid input!")

    def __execute_option_statistics(self, option):
        if "statistics 1" in option:
            for key, value in self.__rental_service.rent_statistic():
                print(str(self.__book_service.find_book_by_id(key)), end="")
                print(f" ||The book was rented {value} times.")
        elif "statistics 2" in option:
            for key, value in self.__rental_service.client_rent_statistic():
                print(str(self.__client_service.find_client_by_id(key)), end="")
                print(f" || The client rented {value} times.")

    def __execute_option(self, option):
        """This function executes the desired option.
        :param option: string
        :return: -
        """
        if "add" in option:
            self.__execute_option_add(option)
        elif "display" in option:
            self.__execute_option_display(option)
        elif "remove" in option:
            self.__execute_option_remove(option)
        elif "update" in option:
            self.__execute_option_update(option)
        elif "rent book" in option:
            rental_id = int(input("Rental ID: "))
            book_id = int(input("Book ID: "))
            client_id = int(input("Client ID: "))
            date = datetime.datetime.now()
            self.__rental_service.add_rental(rental_id, book_id, client_id, date.strftime("%d.%m.%Y"), None)
        elif "return book" in option:
            rental_id = int(input("Rental ID: "))
            self.__rental_service.return_book(rental_id)
        elif "search" in option:
            self.__execute_option_search(option)
        elif "statistics" in option:
            self.__execute_option_statistics(option)
        elif "undo" in option:
            self.__undo_redo_service.undo()
        elif "redo" in option:
            self.__undo_redo_service.redo()
        else:
            print("Invalid input!")

    def __transform_option(self, option):
        if option == "1":
            option = "add book"
        elif option == "2":
            option = "add client"
        elif option == "3":
            option = "remove book"
        elif option == "4":
            option = "remove client"
        elif option == "5":
            option = "display books"
        elif option == "6":
            option = "display clients"
        elif option == "7":
            option = "display rentals"
        elif option == "8":
            option = "update book"
        elif option == "9":
            option = "update client"
        elif option == "10":
            option = "rent book"
        elif option == "11":
            option = "return book"
        elif option == "12":
            option = "search book"
        elif option == "13":
            option = "search client"
        elif option == "14":
            option = "statistics 1"
        elif option == "15":
            option = "statistics 2"
        elif option == "16":
            option = "undo"
        elif option == "17":
            option = "redo"
        elif option == "0":
            option = "exit"
        return option

    def start(self):
        self.__menu()
        while True:
            __option = self.__read_option()
            __option = self.__transform_option(__option)
            if __option == "exit":
                break
            else:
                self.__execute_option(__option)
