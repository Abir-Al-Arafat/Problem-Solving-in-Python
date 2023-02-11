# Implement a hash table
# The hashtable should have prime number of addresses
# Because Prime number increases the amount of randomness which reduces colisions

class HashTable:
    def __init__(self, size=7):
        # initializing a list of none values with default size as a prime number
        self.data_map = [None] * size

    # method for getting the address
    def __hash(self, key):
        my_hash = 0

        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        # returns the address
        return my_hash

    # method for printing the address
    def print_ht(self):
        for address, value in enumerate(self.data_map):
            print(address, ": ", value)

    # method for setting an item in an address
    def set_item(self, key, value):
        # storing index
        index = self.__hash(key)

        # keeping the value in the index
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    # method for getting an item from an address
    def get_item(self, key):
        # storing index
        index = self.__hash(key)

        # returns none if the key doesnt exist
        if self.data_map[index] is None:
            return None

        # iterating over the items and returns the value
        for items in self.data_map[index]:
            if items[0] == key:
                return items[1]

    # method for getting all the keys
    def keys(self):
        all_keys = []
        for list_items in self.data_map:
            if list_items:
                for item in list_items:
                    all_keys.append(item[0])
        return all_keys


ht = HashTable()
print(ht.data_map)
ht.set_item("nuts", 1200)
ht.set_item("bolts", 1200)
ht.set_item("hammer", 200)
ht.set_item("screw", 1500)
ht.set_item("pins", 2000)
ht.set_item("washers", 1400)
ht.set_item("lumber", 400)
ht.print_ht()

print(ht.get_item("washers"))
print(ht.keys())
