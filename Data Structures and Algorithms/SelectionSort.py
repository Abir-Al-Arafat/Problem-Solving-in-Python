# write a function which takes a list of integers as input and sorts the elements according to selection sort algorithm

array = [4, 2, 6, 5, 1, 3]
print(array)


def selection_sort(array):
    # for loop to start from a particular index
    for current_index in range(len(array)-1):
        # setting the current index as minimum index
        min_index = current_index
        # running another for loop to compare the indices with current index
        for compare_index in range(current_index+1, len(array)):
            if array[compare_index] < array[min_index]:
                # setting the minimum index
                min_index = compare_index

        # checing if minimum index is changed after the for loop
        if min_index != current_index:
            # replacing the values in the indices
            temp = array[current_index]
            array[current_index] = array[min_index]
            array[min_index] = temp
            # printing the array with replaced elements
            print(array)


# calling function
selection_sort(array)
