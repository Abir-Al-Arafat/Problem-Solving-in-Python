# bottom - up no memory dynamic programming

def fib(n):
    if n<2: return n

    prev, cur = 0, 1

    for _ in range(2, n+1):
        prev, cur = cur, cur+prev
    
    return cur

print(fib(5))