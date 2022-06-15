# Write a Python program to add two given lists and find the difference between lists. Use map() function.

# Input:

# nums1 = [6, 5, 3, 9]

# nums2 = [0, 1, 7, 7]

# Output:
# [(6, 6), (6, 4), (10, -4), (16, 2)]

nums1 = [2, 4, 6, 8]  # declaring a list

nums2 = [1, 3, 9, 12]  # declaring a list

# a function that returns addition and substraction of the elements


def difference(num1, num2):
    return num1+num2, num1-num2


# map function that takes a function and iterables as inputs
diff = map(difference, nums1, nums2)

print(list(diff))
