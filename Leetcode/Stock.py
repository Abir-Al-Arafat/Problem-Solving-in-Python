# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input: prices = [7,1,5,3,6,4]
# Output: 5

# Input: prices = [7,6,4,3,1]
# Output: 0

def maxProfit(array):
    profit = 0
    index = 0
    buy = array[index]
    for i in range(1, len(array)):
        if array[i] - buy > profit:
            profit = array[i] - buy
        if array[i] - buy < 0 and profit <= 0:
            profit = 0
            index += 1
            buy = array[index]
        if array[i] < buy:
            buy = array[i]
    return profit


prices = [2, 1, 2, 1, 0, 1, 2]
print(maxProfit(prices))
