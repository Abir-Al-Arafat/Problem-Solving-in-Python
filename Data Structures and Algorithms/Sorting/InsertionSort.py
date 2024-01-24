# write a function which takes a list of integers as input and sorts the elements according to insertion sort algorithm

def insertion_sort(array):
    # for loop starts from 2nd index
    for index in range(1, len(array)):
        # keeping the previous index in a variable
        prev = index-1
        # keeping the value of present index in a variable
        now = array[index]

        # loop will run until the value of previous index is bigger than the value of present index
        while array[prev] > now and prev >= 0:
            # swapping elements
            array[prev+1] = array[prev]
            array[prev] = now
            # decrementing to go to further previous index
            prev -= 1
            print(array)


array = [6, 5, 4, 3, 2, 1]

print(array)
insertion_sort(array)
