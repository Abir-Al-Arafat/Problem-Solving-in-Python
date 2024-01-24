# function to merge the list
def merge(list1, list2):
    # empty list to keep the sorted array
    combined = []

    # initializing indices for the arrays
    i = 0
    j = 0

    # loop will keep running until it compared all the elements in both lists
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            # adding element
            combined.append(list1[i])
            # increasing index
            i += 1
        else:
            # adding element
            combined.append(list2[j])
            # increasing index
            j += 1

    # checking if there is any element left behind
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    # checking if there is any element left behind
    while j < len(list2):
        combined.append(list2[j])
        j += 1

    # returning the combined list
    return combined


# function to break the list until there is one element left
def merge_sort(array):
    # base case for recursive function
    if len(array) == 1:
        return array

    # finding the middle index
    mid = len(array)//2

    # dividing the array in two parts

    # left part of the array
    left = array[:mid]
    # right part of the array
    right = array[mid:]

    # recursive case
    # returning the divided array in a merged format
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([10, 5, 3, 1, 4, 2]))
