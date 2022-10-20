from src.domain.client import Client
from src.domain.container import Container
from src.domain.validators import Validators
from openpyxl import load_workbook

class ClientRepository:
    def __init__(self):
        self.__list_of_clients = Container()

    @property
    def list_of_clients(self):
        """This function returns the list of clients.
        :return: the list of clients
        """
        return self.__list_of_clients

    def load_data(self):
        workbook = load_workbook("D:\\GitHub\\a9-luckytoef\\src\\repository\\data\\clients_data.xlsx")
        sheet = workbook.active
        for row in sheet.rows:
            self.__list_of_clients.append(Client(row[0].value, row[1].value))

    def check_if_client_id_is_unique(self, unchecked_id):
        """This function checks if the unchecked_id is unique or not.
        :param unchecked_id: string
        :return: True if unchecked_id is unique, False if not.
        """
        for client in self.__list_of_clients:
            if client.client_id == unchecked_id:
                return False
        return True

    def add_client(self, client_id, name):
        """This function adds a client to the list of clients.

        :param client_id: string
        :param name: string
        :return: -
        """
        if self.check_if_client_id_is_unique(client_id) is True:
            new_client = Client(client_id, name)
            self.__list_of_clients.append(new_client)
        else:
            Validators.handle_not_unique_id()

    def remove_client(self, client_id):
        """This function removes a client from the list of clients.

        :param client_id: integer
        :return: -
        """
        if self.check_if_client_id_is_unique(client_id) is True:
            Validators.entity_not_in_list()
        else:
            for client in self.__list_of_clients:
                if client.client_id == client_id:
                    client_to_be_removed = client
                    self.__list_of_clients.remove(client_to_be_removed)
                    return

    def update_client(self, client_id, new_client):
        """This function updates a client with a new one.

        :param client_id: int
        :param new_client: a client object, class <client>
        :return: -
        """
        index = -1
        if self.check_if_client_id_is_unique(client_id) is True:
            Validators.id_not_in_list()
        elif self.check_if_client_id_is_unique(new_client.client_id):
            for client in self.list_of_clients:
                index += 1
                if client.client_id == client_id:
                    self.__list_of_clients[index] = new_client
                    return
        else:
            Validators.handle_not_unique_id()
