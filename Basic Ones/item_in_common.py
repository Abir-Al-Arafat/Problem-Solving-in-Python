# write a function which takes two arrays as input
# and returns True if they have at least ONE common element
# otherwise returns False
# Time Complexity: O(n)

def item_in_common(item1, item2):
    # initializing dictionary
    compare = {}

    for item in item1:
        compare[item] = True

    for item in item2:
        if item in item1:
            return True

    return False


a = [3, 4, 5]
b = [2, 7, 4]
print(item_in_common(a, b))
