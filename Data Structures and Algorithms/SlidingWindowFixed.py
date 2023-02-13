# Given an array, return true if there are two elements within a window of size K that are equal

array = [1, 2, 3, 2, 3, 3]

# time complexity: O(n*k) or O(n*size)


def bruteForce(array, size):
    for left in range(len(array)):
        for right in range(left+1, min(left+size, len(array))):
            if array[left] == array[right]:
                return True

    return False

# time complexity: O(n)


def slidingWindow(array, size):
    # initializing left boundary
    left = 0
    # initializing set
    window = set()

    for right in range(len(array)):
        # checking if the window goes out of bound
        if (right - left) + 1 > size:
            # removing the element from left boundary
            window.remove(array[left])
            # moving left boundary one step
            left += 1

        # checking if the element exists in the window
        if array[right] in window:
            return True

        # adding element to the window
        window.add(array[right])

    return False


# print(bruteForce(array, 2))
print(slidingWindow(array, 5))
