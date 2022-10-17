# write a function which takes an array and sorts them according to bucket sort algorithm

def bucketSort(array):
    # initializing an array accoring to the highest number inside the array input
    count = [0 for i in range(max(array)+1)]

    # keeping the count of the elements of input according to indices
    for val in array:
        count[val] += 1

    # to keep the count of index
    index = 0

    # iterating the number of indices and putting it in the array in sorted order
    for value in range(len(count)):
        for _ in range(count[value]):
            array[index] = value
            index += 1

    return array


array = [2, 1, 2, 0, 0, 3, 5, 8]
print(max(array))

print(bucketSort(array))
