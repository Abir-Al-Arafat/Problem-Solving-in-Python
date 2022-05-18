# write a function which takes an array of stock prices of a product in different times and returns the maximum profit out of it

def profit(prices):
    # initializing a variable with element of first index as minimum value
    minSoFar = prices[0]
    maxProfit = 0  # initializing max profit with 0

    # running a for loop starting from 2nd index
    for index in range(0, len(prices)):
        # setting the minimum price found in the array
        minSoFar = min(minSoFar, prices[index])
        profit = prices[index] - minSoFar  # setting the profit found so far
        maxProfit = max(profit, maxProfit)  # setting the maximum profit
    return maxProfit  # returning the maximum profit


prices = [5, 2, 6, 1, 4]
print(profit(prices))
