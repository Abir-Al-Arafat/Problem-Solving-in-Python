if min_index != start_index:
        temp = array[start_index]
        array[start_index] = array[min_index]
        array[min_index] = temp
    print(array)