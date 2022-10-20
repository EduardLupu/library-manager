class Container:
    def __init__(self, new_list=None):
        if new_list is None:
            new_list = []
        self.__container = new_list

    def __len__(self):
        return len(self.__container)

    def __setitem__(self, key, value):
        self.__container[key] = value

    def __getitem__(self, key):
        return self.__container[key]

    def __delitem__(self, key):
        del self.__container[key]

    def __iter__(self):
        self.key = -1
        return self

    def __next__(self):
        self.key += 1
        if self.key >= len(self.__container):
            raise StopIteration
        return self.__container[self.key]

    def append(self, item):
        self.__container.append(item)

    def remove(self, item):
        self.__container.remove(item)

    def reverse(self):
        self.__container.reverse()


