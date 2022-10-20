import json
from src.repository.client_repo import ClientRepository


class ClientRepositoryJSON(ClientRepository):
    def __init__(self, clients_text_file):
        super(ClientRepositoryJSON, self).__init__()
        self.__file_name = clients_text_file
        self.__load_data()

    def __load_data(self):
        file = open(self.__file_name, "r")
        for element in json.load(file):
            super().add_client(int(element["id"]), element["name"])
        file.close()

    def __save_data(self):
        file = open(self.__file_name, "w")
        content = []
        for client in super().list_of_clients:
            dictionary = {"id": client.client_id, "name": client.name}
            content.append(dictionary)
        json.dump(content, file, indent=4)
        file.close()

    def add_client(self, client_id, name):
        super(ClientRepositoryJSON, self).add_client(client_id, name)
        self.__save_data()

    def remove_client(self, client_id):
        super(ClientRepositoryJSON, self).remove_client(client_id)
        self.__save_data()

    def update_client(self, client_id, new_client):
        super(ClientRepositoryJSON, self).update_client(client_id, new_client)
        self.__save_data()
