import sqlite3
from src.repository.client_repo import ClientRepository


class ClientRepositoryDatabase(ClientRepository):
    def __init__(self, clients_text_file):
        super(ClientRepositoryDatabase, self).__init__()
        self.__file_name = clients_text_file
        self.__load_data()

    def __load_data(self):
        self.connection = sqlite3.connect(self.__file_name)
        self.cursor = self.connection.cursor()
        self.query = """
        CREATE TABLE IF NOT EXISTS clients (
          id INTEGER PRIMARY KEY,
          name TEXT
        );
        """
        self.cursor.execute(self.query)
        self.connection.commit()
        self.cursor.execute("""SELECT * FROM clients;""")
        rows = self.cursor.fetchall()
        for client in rows:
            super().add_client(client[0], client[1])

    def add_client(self, client_id, name):
        super(ClientRepositoryDatabase, self).add_client(client_id, name)
        self.cursor.execute("""INSERT INTO clients VALUES (?, ?);""", (client_id, name))
        self.connection.commit()

    def remove_client(self, client_id):
        super(ClientRepositoryDatabase, self).remove_client(client_id)
        self.cursor.execute("""DELETE FROM clients WHERE id=?;""", (client_id,))
        self.connection.commit()

    def update_client(self, client_id, new_client):
        super(ClientRepositoryDatabase, self).update_client(client_id, new_client)
        self.cursor.execute("""UPDATE clients SET id=?, name=? WHERE id=?;""",
                            (new_client.client_id, new_client.name, client_id))
        self.connection.commit()
