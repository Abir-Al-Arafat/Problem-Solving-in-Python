# Quick Sort Implementation

array = [4, 6, 1, 7, 3, 2, 5]

# for swapping elements
def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp

# returns pivot index
def pivot_index(array, pivot_idx, end_idx):
    swap_idx = pivot_idx

    for idx in range(pivot_idx+1, end_idx):
        if array[idx] < array[pivot_idx]:
            swap_idx += 1
            swap(array, idx, swap_idx)
    
    swap(array, pivot_idx, swap_idx)

    return swap_idx

# sorts the elements
def quick_sort_helper(array, left, right):
    if left < right:
        pivot_idx = pivot_index(array, left, right)
        quick_sort_helper(array, left, pivot_idx)
        quick_sort_helper(array, pivot_idx+1, right)
    
    return array

def quick_sort(array):
    return quick_sort_helper(array, 0, len(array))

print(array)
print(pivot_index(array, 0, len(array)))
print(quick_sort(array))
# print(array)