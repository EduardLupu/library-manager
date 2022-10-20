from src.repository.client_repo import ClientRepository


class ClientRepositoryFile(ClientRepository):
    def __init__(self, clients_text_file):
        super().__init__()
        self.__file_name = clients_text_file
        self.__load_data()

    def __load_data(self):
        file = open(self.__file_name, "rt")
        for line in file.readlines():
            client_id, name = line.split(", ")
            name = name.removesuffix("\n")
            super().add_client(int(client_id), name)
        file.close()

    def __save_data(self):
        file = open(self.__file_name, "wt")
        for client in super().list_of_clients:
            file.writelines(f"{client.client_id}, {client.name}\n")
        file.close()

    def add_client(self, client_id, name):
        super(ClientRepositoryFile, self).add_client(client_id, name)
        self.__save_data()

    def remove_client(self, client_id):
        super(ClientRepositoryFile, self).remove_client(client_id)
        self.__save_data()

    def update_client(self, client_id, new_client):
        super(ClientRepositoryFile, self).update_client(client_id, new_client)
        self.__save_data()
