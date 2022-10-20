from src.repository.client_repo import ClientRepository
import pickle


class ClientRepositoryBinary(ClientRepository):
    def __init__(self, clients_text_file):
        super().__init__()
        self.__file_name = clients_text_file
        self.__load_data()

    def __load_data(self):
        file = open(self.__file_name, "rb")
        clients = pickle.load(file)
        for client in clients:
            super().add_client(client.client_id, client.name)
        file.close()

    def __save_data(self):
        file = open(self.__file_name, "wb")
        pickle.dump(super().list_of_clients, file)
        file.close()

    def add_client(self, client_id, name):
        super(ClientRepositoryBinary, self).add_client(client_id, name)
        self.__save_data()

    def remove_client(self, client_id):
        super(ClientRepositoryBinary, self).remove_client(client_id)
        self.__save_data()

    def update_client(self, client_id, new_client):
        super(ClientRepositoryBinary, self).update_client(client_id, new_client)
        self.__save_data()
