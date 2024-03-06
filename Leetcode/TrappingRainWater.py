# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

height = [4,2,0,3,2,5]

def trap(height):
    left, right = 0, len(height)-1

    maxLeft, maxRight = height[0], height[len(height)-1]

    maxWater = 0

    while left < right:
        if height[left] < height[right]:
            left += 1
            if maxLeft - height[left] > 0:
                maxWater+=maxLeft - height[left]
            if height[left] > maxLeft:
                maxLeft = height[left]
        else:
            right-=1
            
            if maxRight - height[right] > 0:
                maxWater += maxRight - height[right]

            if height[right] > maxRight:
                maxRight = height[right]

    return maxWater

print(trap(height))

