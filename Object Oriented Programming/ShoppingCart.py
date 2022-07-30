# Write a class called ShoppingCart that might be used in an online store. It should have the following:
# • A list of Item objects that represents the items in the shopping cart.
# 1. A constructor that creates an empty list of items (the constructor should take no arguments except self)
# 2. A method called add_item() that takes a name and a price and adds an Item object with that name and price to the shopping cart
# 3. A method called total() that takes no arguments and returns the total cost of the items in the cart
# 4. A method called remove_items() that takes an item name (a string) and removes any Item objects with that name from the shopping cart. It should return the item that was removed.
# 5. A str_() method that returns a string containing info on all the items in the shopping cart Then test out the shopping cart as follows: (1) create a shopping cart; (2) add several items to it; (3) print the cart's total cost (using the total() method); (4) remove one of the items types; (5) print out the cart.

# declaring a class
class ShoppingCart:
    # constructor
    def __init__(self):
        self.items = {}
        self.length = 0

    # printing items inside the cart
    def print_items(self):
        for key in self.items:
            print(key, self.items[key], end=', ')

    # adding an item
    def add_item(self, item, price):
        self.items[item] = price
        self.length += 1

    # returning the total price
    def total(self):
        self.total = 0
        for key in self.items:
            self.total += self.items[key]
        return self.total

    def remove_item(self, item):
        # dictionary comprehension to remove an item
        self.items = {key: self.items[key]
                      for key in self.items if key != item}
        self.length -= 1

    # magic method to print the items of the cart
    def __str__(self):
        return f"{self.items}"


cart = ShoppingCart()

cart.add_item('cap', 50)
cart.add_item('shirt', 450)
cart.add_item('tshirt', 150)
cart.add_item('socks', 50)
# print(cart.items)
print(cart.length)
print(cart.print_items())
print(cart.total())

cart.remove_item('cap')
print(cart.print_items())
print(cart.length)

print(cart.__str__())
