from src.settings.settings import Settings
from src.services.book_service import BookService
from src.services.client_service import ClientService
from src.services.rental_service import RentalService
from src.undo.undo import UndoRedoService
from src.ui.console import ConsoleUI

if __name__ == '__main__':

    book_repo, client_repo, rental_repo = Settings().get_repos()
    book_service = BookService(book_repo)
    client_service = ClientService(client_repo)
    rental_service = RentalService(rental_repo)
    undo_action = UndoRedoService(book_repo, client_repo, rental_repo)

    Console = ConsoleUI(book_service, client_service, rental_service, undo_action)
    Console.start()
