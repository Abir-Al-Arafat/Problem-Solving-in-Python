# Create a function to convert two different list into one dictionary output as in the example.

# Input:
# stocks = ['Amazon', 'Apple', 'AMD']
# prices = [2921, 702.10, 102.26]
# Output:
# {'Amazon': 2921, 'Apple': 702.10, 'AMD': 102.26}

stocks = ['Amazon', 'Apple', 'AMD']
prices = [2921, 702.10, 102.26]


def listToDict(list1, list2):

    # The Python zip() function accepts iterable items and merges them into a single tuple. The resultant value is a zip object that stores pairs of iterables. Lists, tuples, sets, or dictionaries can be passed through the zip() function

    converted = {stock: price for stock, price in zip(stocks, prices)}
    return converted


# output = zip(stocks, prices)
print(listToDict(stocks, prices))
