# Problem Statement

# Sara is solving a math problem in which she has given an integer N and her task is to find the number of operations required to convert N into 1. Where in one operation you replace the number with its second-highest divisor.

# Output:
# Return the number of operations required.

# Sample Input:-
# 100

# Sample Output:-
# 4

# Explanation:-
# 100 - > 50
# 50 - > 25
# 25 - > 5
# 5 - > 1

# Sample Input:-
# 10

# Sample Output:-
# 2

# declaring a function
def DivisorProblem(N):
    count = 0  # variable to keep the count of number of operations
    # running a while loop until it reaches 1
    while(N > 1):
        for div in range(2, 10):  # for loop to divide the integer
            if N % div == 0:  # checking if the integer can be divisible or not
                N = N//div
                count += 1  # incrementing the value by 1 if can be divisible
    return count  # returning the count


print(DivisorProblem(100))
