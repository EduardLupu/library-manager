class LibraryException(Exception):
    pass


class Validators:
    @staticmethod
    def handle_not_unique_id():
        raise LibraryException("The ID is already in use!")

    @staticmethod
    def book_not_in_excel():
        raise LibraryException("The book is not in the list!")

    @staticmethod
    def client_not_in_excel():
        raise LibraryException("The client is not in the list!")

    @staticmethod
    def id_not_in_list():
        raise LibraryException("The ID is not in the list!")

    @staticmethod
    def entity_not_in_list():
        raise LibraryException("The specified entity is not in the list!")

    @staticmethod
    def book_is_rented():
        raise LibraryException("The specified book is not avaible!")

class UndoValidator:
    @staticmethod
    def validate_undo(stack_pointer):
        if stack_pointer < 0:
            raise LibraryException("Nothing to undo!")

    @staticmethod
    def validate_redo(stack_pointer, stack_length):
        if stack_pointer == stack_length:
            raise LibraryException("Nothing to redo!")