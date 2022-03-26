# Suppose we have a set of 100 items that we are trying to collect. The items are sold in packages of 20 items, with all 20 items in each package being different. Write a program that simulates how long it will take until we have collected all 100 items. Do this by randomly generating packages of 20 and adding them to a collection until that collection has all 100 different items.

from random import sample

# list of 100 items
items = [i for i in range(1, 101)]
# initializing empty list
collection = []
# keeping time to 0
time = 0
# while loop will keep running until the length reaches 100
while len(collection) != 100:
    # choosing 20 items from the list randomly
    package = sample(items, 20)
    # running a for loop for the 20 items set
    for item in package:
        # checking if the items exists in the collection or not
        if item not in collection:
            # adding the item in the collection
            collection.append(item)
            # removing the item from the given list to save time
            items.remove(item)
    time += 1
print(time)
