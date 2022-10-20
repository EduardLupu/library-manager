
class ClientService:
    def __init__(self, client_repo):
        self.__client_repo = client_repo

    def add_client(self, client_id, name):
        # adds a client
        self.__client_repo.add_client(client_id, name)

    def remove_client(self, client_id):
        # removes a client
        self.__client_repo.remove_client(client_id)

    def update_client(self, client_id, new_client):
        # updates a client with a new one
        self.__client_repo.update_client(client_id, new_client)

    def get_all(self):
        return self.__client_repo.list_of_clients

    def find_client_by_id(self, book_id):
        """This function returns the client with the specified id.
        :param book_id:int
        :return:book
        """
        for client in self.get_all():
            if client.client_id == book_id:
                return client
        return None

    def search_client(self, data_of_client):
        """This function search for clients which have a common data.
        :param data_of_client: any data of the client(id/ title/ author)
        :return:
        """
        client_list = []
        found_data = 0
        if data_of_client.isnumeric():
            for client in self.get_all():
                if client.client_id == int(data_of_client):
                    client_list.append(client)
                    found_data = 1
        else:
            for client in self.get_all():
                if data_of_client in client.name.lower():
                    client_list.append(client)
                    found_data = 1
        if found_data:
            return client_list
        return None