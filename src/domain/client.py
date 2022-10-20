
class Client:
    def __init__(self, client_id, name):
        self.__client_id = client_id
        self.__name = name

    @property
    def client_id(self):
        """This function returns the client_id.

        :return: client_id
        """
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        """This function sets the client_id.

        :return: -
        """
        self.__client_id = value

    @property
    def name(self):
        """This function returns the name.

        :return: name
        """
        return self.__name

    @name.setter
    def name(self, value):
        """This function sets the name.

        :return: -
        """
        self.__name = value

    def __str__(self):
        """This function converts a client to string representation.
        :return: a string representation of a object book-
        """
        return f"Client ID: {self.__client_id}, Name: {self.__name}"
