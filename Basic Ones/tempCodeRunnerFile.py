def fastPower(x, y):
    result = 1
    while y > 0:
        if y % 2 != 0:
            result = result*x
        x = x*x
        x = x//2
    return result


print(fastPower(2, 3))