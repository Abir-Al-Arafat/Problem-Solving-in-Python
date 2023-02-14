# Check if an array is a palindrome

array = [1, 3, 9, 9, 3, 1]


def isPalindromeArray(array):
    # setting pointers
    left = 0
    right = len(array) - 1

    # loop for pointers
    while left < right:
        # checking if elements dont match
        if array[left] != array[right]:
            return False
        # shifting pointers
        left += 1
        right -= 1

    return True


print(isPalindromeArray(array))
