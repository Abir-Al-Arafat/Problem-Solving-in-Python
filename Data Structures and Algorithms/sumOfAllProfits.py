# write a function which takes an array of stock prices of a product in different times and returns the sum of all the profits during the period of time

def sumOfProfits(prices):
    profit = 0  # initializing the profit to 0

    # running a for loop starting from 2nd index
    for index in range(1, len(prices)):
        # checking if prevous price was less or not
        if prices[index] > prices[index-1]:
            # adding profit
            profit += prices[index] - prices[index-1]
            # returning profit
    return profit


prices = [5, 2, 6, 1, 4, 7, 3, 6]
print(sumOfProfits(prices))
