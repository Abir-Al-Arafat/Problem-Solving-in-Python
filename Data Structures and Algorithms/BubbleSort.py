# write a function which takes an list of integers as input and sorts the elements according to bubble sort algorithm


def bubble_sort(array):
    # runnning a for loop to decide how many times to go through the array to sort
    for length in range(len(array)-1, 0, -1):
        # running for loop for unsorted elements
        for index in range(length):
            if array[index] > array[index+1]:
                # swapping element to sort
                temp = array[index]
                array[index] = array[index+1]
                array[index+1] = temp
    return array


array = [4, 2, 6, 5, 1, 3]

print(bubble_sort(array))
