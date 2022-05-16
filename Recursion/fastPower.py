# write a function which takes two parameters x,y and returns the the value of x to the power y

def fastPower(x, y):
    if y == 0:
        return 1
    return x*fastPower(x, y-1)


print(fastPower(5, 3))
