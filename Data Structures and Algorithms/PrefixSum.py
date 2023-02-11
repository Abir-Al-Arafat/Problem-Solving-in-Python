# given an array of values, design a data structure that can query the sum of a subarray of the values.

# Time Complexity: O(1)

class PrefixSum:
    def __init__(self, array):
        self.prefixSum = []
        self.total = 0

        # iterating over the array to populate the prefix sum list
        for val in array:
            self.total += val
            self.prefixSum.append(self.total)
    # left and right index as input

    def rangeSum(self, left, right):
        rightVal = self.prefixSum[right]
        # when idx 0 is given as input
        if left == 0:
            return rightVal
        leftVal = self.prefixSum[left-1]
        # returning the sum of the range
        return rightVal - leftVal


array = [2, -1, 3, -3, 4]
ps = PrefixSum(array)

print(ps.prefixSum)
print(ps.rangeSum(0, 1))
