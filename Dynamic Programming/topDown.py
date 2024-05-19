# Top-Down DP (Memoization)
# Time Complexity: O(n)
def fib(n):
    memo = {0:0, 1:1}

    def fibonacci(n):
        if n in memo:
            return memo[n]
        
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]
    
    return fibonacci(n)

print(fib(6))