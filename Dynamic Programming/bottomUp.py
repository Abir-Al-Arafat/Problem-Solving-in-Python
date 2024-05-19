# Bottom - Up DP (Tabulation)

def fib(n):
    dp = [0,1]

    for i in range(2, n+1):
        new = dp[i-2] + dp[i-1]
        dp.append(new)
    
    return dp[n]

print(fib(6))