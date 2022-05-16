# write a function which takes two parameters x,y and returns the the value of x to the power y

def fastPower(x, y):
    res = 1
    while y > 0:
        if y % 2 != 0:
            res = res*x
        x = x*x
        y = y//2
    return res


print(fastPower(2, 5))
