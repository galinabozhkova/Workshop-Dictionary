from copy import deepcopy


class HashTable:
    def __init__(self):
        self.max_length = 4
        self.__keys = [None] * self.max_length
        self.__values = [None] * self.max_length

    def __check_available_index(self, index):
        if index == len(self.__keys):
            index = 0
        if self.__keys[index] == None:
            return index
        return self.__check_available_index(index + 1)

    def __setitem__(self, key, value):
        try:
            index = self.__keys.index(key)
            self.__values[index] = value
            return
        except ValueError:
            if not None in self.__keys:
                self.resize()
            index = self.get_available_index(key)
            self.__keys[index] = key
            self.__values[index] = value

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError("No such key")

    def __len__(self):
        length = len([el for el in self.__keys if el is not None])
        return length

    def __repr__(self):
        dict = self.item()
        return "{" + ', '.join([f'"{el[0]}": "{el[1]}"' for el in dict]) + "}"

    def get_available_index(self, key):
        index = self.hash(key)
        return self.__check_available_index(index)

    def hash(self, key):
        index = sum([ord(el) for el in key]) % self.max_length
        return index

    def resize(self):
        self.__keys = self.__keys + [None] * self.max_length
        self.__values = self.__values + [None] * self.max_length
        self.max_length *=2

    def get(self, key):
        try:
            return self.__getitem__(key)
        except KeyError:
            return None

    def add(self, key, value):
        return self.__setitem__(key, value)

    def keys(self):
        return [el for el in self.__keys if el is not None]

    def values(self):
        return [self.__values[self.__keys.index((el))] for el in self.keys()]

    def item(self):
        return list(zip(self.keys(), self.values()))

    def pop(self, key):
        try:
            index = self.__keys.index(key)
            el = self.__keys[index]
            self.__keys[index] = None
            self.__values[index] = None
            return el
        except ValueError:
            raise KeyError("Invalid key")

    def copy(self):
        return deepcopy(self)

    def clear(self):
        length = len(self.__keys)
        self.__keys = [None] * length
        self.__values = [None] * length


# table = HashTable()
#
# table["name"] = "Peter"
# table["age"] = 25
# table["gea"] = "rfgrg"
# table["ega"] = "rfgrg"
# table["page"] = 28
#
# abc = table.copy()
#
# print(table)
# print(table.get("name"))
# print(table["age"])
# print(len(table))
# print(table.item())
# table.pop("name")
# print(table.item())
# print(table)
# print(table.get("bktt"))
#
# print(table)
# table1 = table.copy()
# print(table1)
